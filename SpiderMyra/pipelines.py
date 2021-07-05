from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter
import numpy as np


class SpidermyraPipeline:

    def process_item(self, item, spider):
        if(("life" in item['tags']) and ('Mark Twain' in item['autor'])):
            print('')
            print('--------------- REGRA 1 - TAG: "life" ------------------')
            print(item)
            print('Exporta csv...\n')
        
            

