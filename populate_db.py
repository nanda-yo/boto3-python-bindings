from db.db import initialize_db
from db.domain import ItemsDomain, ItemsRepository
from fakefakerheh.faker_items import ItemsFactory
import time

def populate_db():
    db = initialize_db()
    items_repo = ItemsRepository(db)
    items_domain = ItemsDomain(items_repo)
    items_domain.create_item(ItemsFactory.build())

# export AWS specific values for this to work

if __name__ == "__main__":
    start= time.process_time()

    for foo in range(0,1):
        populate_db()

    print(time.process_time() - start)


