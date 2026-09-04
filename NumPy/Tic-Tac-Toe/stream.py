"""A two-player Tic-Tac-Toe game built with Streamlit and NumPy."""

import numpy as np
import streamlit as st


def check_winner(board: np.ndarray) -> str | None:
    """Return the winner (X/O), DRAW, or None while the game continues."""
    row_sums = np.sum(board, axis=1)
    column_sums = np.sum(board, axis=0)
    diagonal_sums = (np.trace(board), np.trace(np.fliplr(board)))

    if 3 in row_sums or 3 in column_sums or 3 in diagonal_sums:
        return "X"
    if -3 in row_sums or -3 in column_sums or -3 in diagonal_sums:
        return "O"
    if not 0 in board:
        return "DRAW"
    return None


def new_game() -> None:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current_player = 1
    st.session_state.result = None


def make_move(row: int, column: int) -> None:
    """Place the current player's mark, then update the game state."""
    if st.session_state.result is not None or st.session_state.board[row, column] != 0:
        return

    st.session_state.board[row, column] = st.session_state.current_player
    st.session_state.result = check_winner(st.session_state.board)

    if st.session_state.result is None:
        st.session_state.current_player *= -1


st.set_page_config(page_title="Tic-Tac-Toe", page_icon="❌", layout="centered")

if "board" not in st.session_state:
    new_game()

st.title("❌ Tic-Tac-Toe ⭕")
st.caption("A local two-player game")

result = st.session_state.result
if result == "DRAW":
    st.info("It’s a draw!")
elif result:
    st.success(f"{result} wins! 🎉")
else:
    player = "X" if st.session_state.current_player == 1 else "O"
    st.subheader(f"{player}'s turn")

symbols = {0: "", 1: "X", -1: "O"}
for row in range(3):
    columns = st.columns(3)
    for column in range(3):
        value = st.session_state.board[row, column]
        columns[column].button(
            symbols[value] or " ",
            key=f"cell-{row}-{column}",
            disabled=value != 0 or result is not None,
            use_container_width=True,
            on_click=make_move,
            args=(row, column),
        )

st.button("New game", on_click=new_game, use_container_width=True)
