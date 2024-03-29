import socket
import asyncio


def create_socket(host='0.0.0.0', port=8000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()

    return sock


async def client_handler(app, coro, _sock):
    loop = asyncio.get_running_loop()
    _sock.send(
        await coro(
            app,
            await loop.sock_recv(_sock, 1024),
            _sock.getpeername()
        )
    )
    _sock.close()


async def main(app, coro, sock: socket.socket):
    loop = asyncio.get_running_loop()
    while True:
        _sock, _ = await loop.sock_accept(sock)
        result = asyncio.create_task(
            client_handler(app, coro, _sock))


def run_server(app, coro):
    return asyncio.run(
        main(
            app,
            coro,
            create_socket(
                app.settings.SERVER_HOST,
                app.settings.SERVER_PORT
            )
        )
    )
