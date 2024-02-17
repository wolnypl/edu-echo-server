from socket import gethostname, socket, AF_INET, SOCK_STREAM, setdefaulttimeout
import os

def application(environ, start_response):
    status = '200 OK'
    # Pobranie zawartości zmiennej środowiskowej WERSJA
    wersja_systemu = os.getenv('WERSJA', 'Nieznana wersja')
    
    # Dodanie informacji o hostname i wersji systemu
    output = f"Hello World!\nMoj hostname to: {gethostname()}\nMoja wersja to: {wersja_systemu}\n".encode()

    # Sprawdzenie, czy zmienna BACKEND jest zdefiniowana
    backend = os.getenv('BACKEND')
    if backend:
        # Ustawienie timeoutu dla połączenia
        setdefaulttimeout(1)
        with socket(AF_INET, SOCK_STREAM) as sock:
            # Próba połączenia się z portem 3306 na hoście określonym przez BACKEND
            result = sock.connect_ex((backend, 3306))
            if result == 0:
                # Port 3306 jest otwarty
                output += f"Port 3306 na hoście {backend} jest otwarty.\n".encode()
            else:
                # Port 3306 jest zamknięty lub nie można się z nim połączyć
                output += f"Port 3306 na hoście {backend} jest zamknięty lub nieosiągalny.\n".encode()
    else:
        # Zmienna BACKEND nie jest zdefiniowana
        output += b"BACKEND nie zdefiniowany.\n"

    # Sprawdzenie, czy plik istnieje
    if os.path.exists('/katalog/plik'):
        output += b"Plik /katalog/plik istnieje, oto jego zawartosc:\n"

        with open('/katalog/plik', 'r') as f_reader:
            for line in f_reader:
                output += f"{line}".encode()
        
        output += b"\nKoniec zawartosci /katalog/plik\n"

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

