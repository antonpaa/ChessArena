from concurrent import futures
import logging

import grpc

import GameManager_pb2
import GameManager_pb2_grpc

class GameManager(GameManager_pb2_grpc.GameService):
    def __init__(self):
        self._gameObject = None
        self._player1 = None
        self._player2 = None
        self._game = None

    def Initialize(self, request, context):
        print("Got a client Initialize call!")
        self._player1 = request.name
        act = GameManager_pb2.Move()
        
        if request.WhichOneof("game") == 'chess':
           module = __import__('chessarena', fromlist=[''])
           self._gameObject = module.ChessArena()
           self._game = 'chess'
           act = GameManager_pb2.Move(chess=GameManager_pb2.ChessMove(), diagnostics='Init')
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Unknown game')
            context.abort_with_status('Client requested game was not known')

        return GameManager_pb2.GameStartInformation(start=True, chessMove=act)

    def Act(self, request_iterator, context):
        print("Got a client Act call!")
        if self._game == 'chess':
            self._gameObject.Act()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GameManager_pb2_grpc.add_GameServiceServicer_to_server(GameManager(), server)
    server.add_insecure_port('192.168.0.11:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
