from concurrent import futures
import logging

import grpc

import ChessArena_pb2
import ChessArena_pb2_grpc

import chessarena

Player1 = ""
Player2 = ""
GameModule

class ChessArena(ChessArena_pb2_grpc.ChessArena):

    def Initialize(self, request, context):
        print("Got a client call!")
        Player1 = request.name
        
        if request.WhichOneof("game") == "chess":
           GameModule = __import__(chessarena, fromlist=[''])
        else:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Unknown game')
            context.set
            return None

        move = ChessArena_pb2.Move()
        return ChessArena_pb2.GameStartInformation(white_player=True, opponent_move=move)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ChessArena_pb2_grpc.add_ChessArenaServicer_to_server(ChessArena(), server)
    server.add_insecure_port('192.168.0.11:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
