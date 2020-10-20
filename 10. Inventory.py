journal = input().split(', ')

command = input()


def collect(item):
    if item not in journal:
        journal.append(item)
    return journal


def drop(item):
    if item in journal:
       journal.remove(item)
    return journal
    
    
def renew(item):
    if item in journal:
       journal.remove(item)
       journal.append(item)
    return journal
       
  
def combine_items(item):
    old_item, new_item = item.split(':')
    if old_item in journal:
       journal.insert(journal.index(old_item)+1, new_item)
    return journal

while command != 'Craft!':
    
    action, item = command.split(' - ')
    
    if action == 'Collect':
       collect(item)
    elif action == 'Drop':
       drop(item)
    elif action == 'Combine Items':
       combine_items(item)
    elif action == 'Renew':
       renew(item)

    command = input()

print(', '.join(journal))
