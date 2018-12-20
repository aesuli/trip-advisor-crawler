
import argparse
import codecs
import csv
import fnmatch
import html
import os
import re


def get_review_filesnames(input_dir):
    for root, dirnames, filenames in os.walk(input_dir):
        for filename in fnmatch.filter(filenames, '*.html'):
            yield os.path.join(root, filename)


hotelnamere = re.compile(r'"description" content="(.*?): ')
block = re.compile(r'"reviewBody":(.*?)"priceRange"')
rating_block = re.compile(r'ratingValue":"(.*?)"},')


def main():
    parser = argparse.ArgumentParser(
        description='TripAdvisor Hotel parser')
    parser.add_argument('-d', '--dir', help='Directory with the data for parsing', required=True)
    parser.add_argument('-o', '--outfile', help='Output file path for saving the reviews in csv format', required=True)

    args = parser.parse_args()


    with codecs.open(args.outfile, 'w', encoding='utf8') as out:
        writer = csv.writer(out, lineterminator='\n')
        for filepath in get_review_filesnames(args.dir):
            with codecs.open(filepath, mode='r', encoding='utf8') as file:
                htmlpage = file.read()
            print(filepath)
            hotelname = hotelnamere.findall(htmlpage)[0]

            try:
                reviewtext = block.findall(htmlpage)[0].split('","',1)[0]
                overallrating = int(rating_block.findall(block.findall(htmlpage)[0].split('","',1)[1])[0])
            except IndexError:
                continue
            if overallrating >= 4:
                binaryrating = 'positive'
            else:
                binaryrating = 'negative'

            review = [filepath, hotelname, reviewtext, overallrating, binaryrating]
            writer.writerow(review)


if __name__ == '__main__':
    main()
