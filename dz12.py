import os

def import_contacts(filename):
  """Импортирует контакты из текстового файла.

  Args:
    filename: Имя текстового файла.

  Returns:
    Словарь с контактами: {фамилия: {имя: имя, отчество: отчество, телефон: телефон}}
  """

  contacts = {}
  with open(filename, "r", encoding="utf-8") as file:
    for line in file:
      surname, name, patronymic, phone = line.strip().split(";")
      contacts.setdefault(surname, {})[name] = {
          "отчество": patronymic,
          "телефон": phone
      }
  return contacts

def export_contacts(filename, contacts):
  """Экспортирует контакты в текстовый файл.

  Args:
    filename: Имя текстового файла.
    contacts: Словарь с контактами.
  """

  with open(filename, "w", encoding="utf-8") as file:
    for surname, data in contacts.items():
      for name, info in data.items():
        file.write(f"{surname};{name};{info['отчество']};{info['телефон']}n")

def search_contacts(contacts, search_term):
  """Ищет контакты по заданному критерию.

  Args:
    contacts: Словарь с контактами.
    search_term: Строка для поиска.

  Returns:
    Список найденных контактов.
  """

  found_contacts = []
  for surname, data in contacts.items():
    if search_term.lower() in surname.lower():
      for name, info in data.items():
        found_contacts.append(f"Фамилия: {surname}, Имя: {name}, Отчество: {info['отчество']}, Телефон: {info['телефон']}")
    for name, info in data.items():
      if search_term.lower() in name.lower() or search_term.lower() in info["отчество"].lower():
        found_contacts.append(f"Фамилия: {surname}, Имя: {name}, Отчество: {info['отчество']}, Телефон: {info['телефон']}")
  return found_contacts

def main():
  """Главная функция программы."""

  contacts_file = "contacts.txt"
  contacts = {}

  if os.path.exists(contacts_file):
    contacts = import_contacts(contacts_file)

  while True:
    print("nТелефонный справочник")
    print("1. Показать контакты")
    print("2. Добавить контакт")
    print("3. Изменить контакт")
    print("4. Удалить контакт")
    print("5. Найти контакт")
    print("6. Сохранить контакты")
    print("7. Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
      if contacts:
        for surname, data in contacts.items():
          for name, info in data.items():
            print(f"Фамилия: {surname}, Имя: {name}, Отчество: {info['отчество']}, Телефон: {info['телефон']}")
      else:
        print("Справочник пуст.")
    elif choice == "2":
      surname = input("Введите фамилию: ")
      name = input("Введите имя: ")
      patronymic = input("Введите отчество: ")
      phone = input("Введите номер телефона: ")
      contacts.setdefault(surname, {})[name] = {
          "отчество": patronymic,
          "телефон": phone
      }
      print("Контакт добавлен.")

    elif choice == "3":
      if contacts:
        surname = input("Введите фамилию контакта для изменения: ")
        if surname in contacts:
          name = input("Введите имя контакта для изменения: ")
          if name in contacts[surname]:
            new_patronymic = input("Введите новое отчество (пусто для сохранения старого): ")
            new_phone = input("Введите новый номер телефона (пусто для сохранения старого): ")
            contacts[surname][name]["отчество"] = new_patronymic if new_patronymic else contacts[surname][name]["отчество"]
            contacts[surname][name]["телефон"] = new_phone if new_phone else contacts[surname][name]["телефон"]
            print("Контакт изменен.")
          else:
            print("Контакт не найден.")
        else:
          print("Контакт не найден.")
      else:
        print("Справочник пуст.")

    elif choice == "4":
      if contacts:
        surname = input("Введите фамилию контакта для удаления: ")
        if surname in contacts:
          name = input("Введите имя контакта для удаления: ")
          if name in contacts[surname]:
            del contacts[surname][name]
            print("Контакт удален.")
          else:
            print("Контакт не найден.")
        else:
          print("Контакт не найден.")
      else:
        print("Справочник пуст.")

    elif choice == "5":
      search_term = input("Введите фамилию, имя или отчество для поиска: ")
      found_contacts = search_contacts(contacts, search_term)
      if found_contacts:
        for contact in found_contacts:
          print(contact)
      else:
        print("Контакты не найдены.")

    elif choice == "6":
      export_contacts(contacts_file, contacts)
      print("Контакты сохранены.")

    elif choice == "7":
      print("До свидания!")
      break

    else:
      print("Неверный выбор.")

if __name__ == "__main__":
  main()