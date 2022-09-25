from mrjob.job import MRJob
from mrjob.step import MRStep


class MRAnalyzePokemons(MRJob):
    total_pokemons = 151

    def steps(self):
        return [
            MRStep(mapper=self.mapper),
            MRStep(reducer=self.reducer),
            MRStep(mapper=self.mapper_avg_damage)
        ]

    def mapper(self, _, line):
        colums = line.split(',')

        for type in colums[4].split(';'):
            yield 'count_type_{}'.format(type.replace('"', '')), 1,

        yield 'count_pokemons', 1,
        yield 'avg_damage_normal', float(colums[6]),
        yield 'avg_damage_fire', float(colums[7]),
        yield 'avg_damage_water', float(colums[8]),
        yield 'avg_damage_electric', float(colums[9]),
        yield 'avg_damage_grass', float(colums[10]),
        yield 'avg_damage_ice', float(colums[11]),
        yield 'avg_damage_fighting', float(colums[12]),
        yield 'avg_damage_poison', float(colums[13]),
        yield 'avg_damage_ground', float(colums[14]),
        yield 'avg_damage_flying', float(colums[15]),
        yield 'avg_damage_psychict', float(colums[16]),
        yield 'avg_damage_bug', float(colums[17]),
        yield 'avg_damage_rock', float(colums[18]),
        yield 'avg_damage_ghost', float(colums[19]),
        yield 'avg_damage_dragon', float(colums[20]),

    def reducer(self, key, values):
        yield (key, sum(values))

    def mapper_avg_damage(self, key, value):
        if key.startswith('avg'):
            yield (key, value / self.total_pokemons)
        else:
            yield (key, value)


if __name__ == '__main__':
    MRAnalyzePokemons.run()
