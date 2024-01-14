def get_api_key(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except IOError:
        print("Error: API_KEYS not exists, check your api keys.")
        return None