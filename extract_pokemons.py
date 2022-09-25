import scrapy


class ExtractPokemons(scrapy.Spider):
    name = 'extract_pokemons'
    start_urls = ['https://www.serebii.net/pokedex/001.shtml']

    def parse(self, response):
        NUMBER_SELECTOR = 'body > div#wrapper:nth-child(3) > div#content:nth-child(5) > main:nth-child(2) > div > div:nth-child(2) > table.dextable:nth-child(5) tr:nth-child(2) td:nth-child(3)::text'

        NAME_SELECTOR = 'body > div#wrapper:nth-child(3) > div#content:nth-child(5) > main:nth-child(2) > div > div:nth-child(2) > table.dextable:nth-child(5) tr:nth-child(2) td:nth-child(1)::text'

        WEIGHT_SELECTOR = 'body > div#wrapper:nth-child(3) > div#content:nth-child(5) > main:nth-child(2) > div > div:nth-child(2) > table.dextable:nth-child(5) tr:nth-child(4) td:nth-child(3)::text'

        HEIGHT_SELECTOR = 'body > div#wrapper:nth-child(3) > div#content:nth-child(5) > main:nth-child(2) > div > div:nth-child(2) > table.dextable:nth-child(5) > tr:nth-child(4) > td:nth-child(2)::text'

        TYPE_SELECTOR = 'body > div#wrapper:nth-child(3) > div#content:nth-child(5) > main:nth-child(2) > div > div:nth-child(2) > table.dextable:nth-child(5) tr:nth-child(2) td:nth-child(4) a::attr(href)'

        DAMAGE_TYPE_SELECTOR = 'body > div#wrapper:nth-child(3) > div#content:nth-child(5) > main:nth-child(2) > div > div:nth-child(2) > table.dextable:nth-child(7) tr:nth-child(2) td a::attr(href)'

        DAMAGE_TAKEN_SELECTOR = 'body > div#wrapper:nth-child(3) > div#content:nth-child(5) > main:nth-child(2) > div > div:nth-child(2) > table.dextable:nth-child(7) tr:nth-child(3) td::text'

        NEXT_SELECTOR = 'body > div#wrapper:nth-child(3) aside table tr:nth-child(2) td:nth-child(3) a'

        EVOLUTION_SELECTOR = 'body > div#wrapper:nth-child(3) > div#content:nth-child(5) > main:nth-child(2) > div > div:nth-child(2) > table.dextable:nth-child(8) .evochain a::attr(href)'

        number = response.css(NUMBER_SELECTOR).get()
        name = response.css(NAME_SELECTOR).get()
        heights = response.css(HEIGHT_SELECTOR).extract()
        height = ''
        weights = response.css(WEIGHT_SELECTOR).extract()
        weight = ''
        types = [type.extract() for type in response.css(TYPE_SELECTOR)]
        damage_types = [type.extract()
                        for type in response.css(DAMAGE_TYPE_SELECTOR)]
        damage_taken = [type.extract()
                        for type in response.css(DAMAGE_TAKEN_SELECTOR)]
        damage_taken_by_type = dict(zip(damage_types, damage_taken))

        evolutions = [evolution.extract()
                      for evolution in response.css(EVOLUTION_SELECTOR)]

        next_evolution_number = int(number.replace('#', '')) + 1

        next_evolution = next((evolution for evolution in evolutions if evolution.find(
            str(next_evolution_number)) > - 1), '')

        if len(heights) > 0:
            height = heights[len(heights) - 1].strip()

        if len(weights) > 0:
            weight = weights[len(weights) - 1].strip()

        yield {
            'number': number,
            'name': name,
            'height': height,
            'weight': weight,
            'types': types,
            'damage_takens': damage_taken_by_type,
            'next_evolution': next_evolution
        }

        for next_page in response.css(NEXT_SELECTOR):
            yield response.follow(next_page, self.parse)
