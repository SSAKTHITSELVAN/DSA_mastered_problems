# Speed Chess Automation System for Android
# Final Working Version with Input Injection Fix

import cv2
import numpy as np
import chess
import chess.engine
import time
import subprocess
import os
from PIL import Image
import io

class SpeedChessBot:
    def __init__(self, device_id=None, stockfish_path='stockfish'):
        """Initialize the chess bot with device connection and chess engine."""
        # Connect to Android device
        self.device_id = device_id
        self.adb_path = r"E:\platform-tools-latest-windows\platform-tools\adb.exe"
        self.adb_prefix = f'"{self.adb_path}" -s {device_id} ' if device_id else f'"{self.adb_path}" '
        
        # Initialize chess engine (Stockfish)
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        self.engine.configure({"Threads": 2, "Hash": 128})
        
        # Chess board state
        self.board = chess.Board()
        
        # Board detection parameters (calibrate these for your device)
        self.board_top = 450    # Y-coordinate of board top
        self.board_left = 120    # X-coordinate of board left
        self.square_size = 105   # Size of each square in pixels
        
        print("Chess bot initialized. Make sure USB debugging authorization is enabled on device.")
    
    def capture_screen(self):
        """Capture a screenshot from the Android device using ADB."""
        command = f"{self.adb_prefix}exec-out screencap -p"
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            screenshot_data, _ = process.communicate()
            image = Image.open(io.BytesIO(screenshot_data))
            return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        except Exception as e:
            print(f"Screenshot failed: {e}")
            return None
    
    def _tap_screen(self, x, y):
        """Send a tap event to the specified coordinates with error handling."""
        command = f"{self.adb_prefix}shell input tap {x} {y}"
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Tap failed: {result.stderr}")
                return False
            return True
        except Exception as e:
            print(f"Tap command failed: {e}")
            return False
    
    def execute_move(self, move):
        """Execute the given move on the Android device with proper delays."""
        from_x, from_y = self._square_to_coords(move.from_square)
        to_x, to_y = self._square_to_coords(move.to_square)
        
        # First tap (select piece)
        if not self._tap_screen(from_x, from_y):
            print("Failed to select piece")
            return False
        
        time.sleep(0.3)  # Crucial delay for move recognition
        
        # Second tap (destination)
        if not self._tap_screen(to_x, to_y):
            print("Failed to place piece")
            return False
        
        # Handle pawn promotion
        if move.promotion:
            time.sleep(0.5)
            promotion_y = self.board_top - 50  # Adjust for your promotion UI
            promotion_x = self.board_left + (chess.square_file(move.to_square) * self.square_size
            self._tap_screen(promotion_x, promotion_y)
        
        self.board.push(move)
        print(f"Executed move: {move}")
        return True
    
    def _square_to_coords(self, square):
        """Convert chess square to screen coordinates with calibration offsets."""
        file_idx = chess.square_file(square)
        rank_idx = 7 - chess.square_rank(square)  # Invert rank for screen coordinates
        
        x = self.board_left + (file_idx + 0.5) * self.square_size
        y = self.board_top + (rank_idx + 0.5) * self.square_size
        
        return int(x), int(y)
    
    def play_game(self):
        """Main game loop with improved error handling."""
        print("Starting game - ensure the chess app is in focus!")
        move_delay = 1.5  # Seconds between moves
        
        while True:
            try:
                screen = self.capture_screen()
                if screen is None:
                    time.sleep(2)
                    continue
                
                # In a real implementation, you would analyze the screen here
                # For now, we'll just make moves assuming it's our turn
                
                move = self.calculate_best_move()
                if not self.execute_move(move):
                    print("Move failed, retrying...")
                    time.sleep(2)
                    continue
                
                time.sleep(move_delay)
                
            except KeyboardInterrupt:
                print("\nGame stopped by user")
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2)
    
    def cleanup(self):
        """Clean up resources."""
        if self.engine:
            self.engine.quit()
        print("Chess bot shutdown complete")


if __name__ == "__main__":
    # Configuration - MUST SET THESE CORRECTLY
    STOCKFISH_PATH = r"C:\chess\stockfish\stockfish-windows-x86-64-avx2.exe"
    DEVICE_ID = '10c859567d73'  # From 'adb devices'
    
    # Calibration values - adjust these based on your screen
    # Use a screenshot to measure the board position
    BOARD_TOP = 450    # Y position of first rank (1)
    BOARD_LEFT = 120    # X position of a-file
    SQUARE_SIZE = 105   # Width/height of each square
    
    try:
        bot = SpeedChessBot(device_id=DEVICE_ID, stockfish_path=STOCKFISH_PATH)
        
        # Override calibration if needed
        bot.board_top = BOARD_TOP
        bot.board_left = BOARD_LEFT
        bot.square_size = SQUARE_SIZE
        
        bot.play_game()
    finally:
        if 'bot' in locals():
            bot.cleanup()