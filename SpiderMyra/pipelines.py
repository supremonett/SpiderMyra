from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter
import re


class SpidermyraPipeline:

    def process_item(self, item, spider):
        item['texto'] = self.chr_remove(item['texto'])

        if(("life" in item['tags']) and ('Mark Twain' in item['autor'])):
            print('')
            print('--------------- REGRA 1 - Tag: "life" ------------------')
            print(item)
            print('Exporta csv...\n')

        if 'truth' in item['texto']:
            print('')
            print('--------------- REGRA 2 - Palavra: "truth" ------------------')
            print(item)
            print('Exporta csv...\n')

    def chr_remove(self, string):
        return re.sub('[^A-Za-z0-9]+', ' ', string)
