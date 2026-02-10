from typing import List, Dict

def filter_adults(users: List[Dict[str, int | str]]) -> List[Dict[str, int | str]]:
    """
    Возвращает список пользователей, возраст которых 18 лет и старше.
    
    Предполагается, что каждый пользователь — словарь с ключами:
    - 'name' (str)
    - 'age' (int)
    """
    return [user for user in users if user["age"] >= 18]

# Пример использования
if __name__ == "__main__":
    test_users: List[Dict[str, int | str]] = [
        {"name": "Алиса", "age": 25},
        {"name": "Боб", "age": 17},
        {"name": "Вася", "age": 30},
        {"name": "Галя", "age": 16}
    ]
    
    adults = filter_adults(test_users)
    print("Совершеннолетние пользователи:")
    for user in adults:
        print(f"- {user['name']}, {user['age']} лет")
