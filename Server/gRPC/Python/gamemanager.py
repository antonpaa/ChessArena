from concurrent import futures
import logging

import grpc

import GameManager_pb2
import GameManager_pb2_grpc

class GameManager(GameManager_pb2_grpc.GameService):
    def __init__(self):
        self._gameModule = None
        self._player1 = None
        self._player2 = None
        self._game = None 

    def Initialize(self, request, context):
        print("Got a client Initialize call!")
        self._player1 = request.name
        
        if request.WhichOneof("game") == 'chess':
           self._gameModule = __import__('chessarena', fromlist=[''])
           self._game = 'chess'
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Unknown game')
            context.abort_with_status('Client requested game was not known')

        act = GameManager_pb2.ChessMove()
        return GameManager_pb2.GameStartInformation(start=True, opponentAct=act)

    def Act(self, request_iterator, context):
        print("Got a client Act call!")
        if self._game == 'chess':
            prevMoves = []
            for newMove in request_iterator:
                for prevMove in prevMoves:
                    if prevMove.game.chess == newMove.game.chess:
                        yield prevMove
                prevMoves.append(newMove)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GameManager_pb2_grpc.add_GameServiceServicer_to_server(GameManager(), server)
    server.add_insecure_port('192.168.0.11:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
