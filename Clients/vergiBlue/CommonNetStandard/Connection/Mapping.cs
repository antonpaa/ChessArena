using CommonNetStandard.Interface;
using CommonNetStandard.Local_implementation;
using GameManager;

namespace CommonNetStandard.Connection
{
    public class Mapping
    {
        public static ChessMove ToGrpc(IMove move)
        {
            var grpcMove = new ChessMove()
            {
                Castling = move.Castling,
                Check = move.Check,
                CheckMate = move.CheckMate,
                StartPosition = move.StartPosition,
                EndPosition = move.EndPosition,
                PromotionResult = (ChessMove.Types.PromotionPieceType) move.PromotionResult
            };
            return grpcMove;
        }

        public static Move ToGrpc(IPlayerMove playerMove)
        {
            var grpcMove = new Move()
            {
                Diagnostics = playerMove.Diagnostics,
                Chess = ToGrpc(playerMove.Move)
            };
            return grpcMove;
        }

        public static IMove ToCommon(Move grpcMove)
        {
            var chessMove = grpcMove.Chess;
            var move = new MoveImplementation()
            {
                Castling = chessMove.Castling,
                Check = chessMove.Check,
                CheckMate = chessMove.CheckMate,
                StartPosition = chessMove.StartPosition,
                EndPosition = chessMove.EndPosition,
                PromotionResult = (PromotionPieceType)chessMove.PromotionResult
            };
            return move;
        }

        
    }
}
