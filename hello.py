from socket import gethostname
import os

def application(environ, start_response):
    status = '200 OK'
    # Pobranie zawartości zmiennej środowiskowej WERSJA
    wersja_systemu = os.getenv('WERSJA', 'Nieznana wersja')
    
    # Dodanie informacji o hostname i wersji systemu
    output = f"Hello World!\nMoj hostname to: {gethostname()}\nMoja wersja to: {wersja_systemu}\n".encode()

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

