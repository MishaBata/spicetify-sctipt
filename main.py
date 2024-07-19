import psutil
import subprocess
import time
import sys

def is_spotify_running():
    "Проверяет, запущен ли процесс Spotify."
    for proc in psutil.process_iter(['pid', 'name']):
        if 'spotify' in proc.info['name'].lower():
            return True
    return False

def run_spicetify_apply():
    "Выполняет команду spicetify apply."
    try:
        subprocess.run(['spicetify', 'apply'], check=True)
        print("Команда 'spicetify apply' выполнена успешно.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды 'spicetify apply': {e}", file=sys.stderr)

def main():
    while True:
        if is_spotify_running():
            print("Spotify запущен.")
        else:
            print("Spotify не запущен. Выполняю команду 'spicetify apply'.")
            run_spicetify_apply()

        # Подождать 10 секунд перед следующей проверкой
        time.sleep(10)

if __name__ == "__main__":
    main()
