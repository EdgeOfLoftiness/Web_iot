from django_seed import Seed
from your_app_name.models import PC, GPU, CPU, Fan, Motherboard

seeder = Seed.seeder()

seeder.add_entity(PC, 5, {
    'name': lambda x: seeder.faker.word(),
})

seeder.add_entity(GPU, 5, {
    'name': lambda x: seeder.faker.word(),
})

seeder.add_entity(CPU, 5, {
    'name': lambda x: seeder.faker.word(),
})

seeder.add_entity(Fan, 5, {
    'name': lambda x: seeder.faker.word(),
})

seeder.add_entity(Motherboard, 5, {
    'name': lambda x: seeder.faker.word(),
})

seeder.execute()
