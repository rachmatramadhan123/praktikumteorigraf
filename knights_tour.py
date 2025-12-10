import matplotlib.pyplot as plt

# --- Knight's Tour Algorithm ---
N = 8
move_x = [1, 1, 2, 2, -1, -1, -2, -2]
move_y = [2, -2, 1, -1, 2, -2, 1, -1]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def get_degree(x, y, board):
    count = 0
    for i in range(8):
        if is_valid(x + move_x[i], y + move_y[i], board):
            count += 1
    return count

def solve_knights_tour(start_x, start_y):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[start_x][start_y] = 0
    curr_x, curr_y = start_x, start_y
    
    # Simpan urutan koordinat untuk plotting (x, y)
    path_x = [start_x]
    path_y = [start_y]

    for i in range(N * N - 1):
        next_x, next_y = -1, -1
        min_deg = 9
        
        # Cari next move terbaik (Warnsdorff)
        for k in range(8):
            nx, ny = curr_x + move_x[k], curr_y + move_y[k]
            if is_valid(nx, ny, board):
                c = get_degree(nx, ny, board)
                if c < min_deg:
                    min_deg = c
                    next_x, next_y = nx, ny
        
        if next_x == -1: 
            return False, [], [], False  # Gagal

        board[next_x][next_y] = i + 1
        curr_x, curr_y = next_x, next_y
        path_x.append(next_x)
        path_y.append(next_y)

    # Cek Closed Tour
    is_closed = False
    for k in range(8):
        if (curr_x + move_x[k] == start_x) and (curr_y + move_y[k] == start_y):
            is_closed = True
            # Tambahkan garis kembali ke awal untuk visualisasi loop
            path_x.append(start_x)
            path_y.append(start_y)
            break
            
    return True, path_x, path_y, is_closed

def display_board(piece_position=None):
    """
    Papan Catur 8x8
    piece_position: tuple (x, y) dimana x=1-8 (kiri ke kanan), y=1-8 (bawah ke atas)
    """
    print("\n  1 2 3 4 5 6 7 8")
    print("  ----------------")
    
    # Loop dari y=8 ke y=1 (dari atas ke bawah untuk tampilan)
    for y in range(8, 0, -1):
        row = f"{y}|"
        for x in range(1, 9):
            if piece_position and piece_position == (x, y):
                row += "♘ "  # Kuda catur
            else:
                # Pola papan catur (kotak hitam dan putih)
                if (x + y) % 2 == 0:
                    row += "■ "  # Kotak gelap
                else:
                    row += "□ "  # Kotak terang
        row += f"|{y}"
        print(row)
    
    print("  ----------------")
    print("  1 2 3 4 5 6 7 8")

def parse_input(input_str):
    """
    Format input: xy (x=horizontal 1-8, y=vertikal 1-8)
    Contoh: "18" -> (1, 8) [kiri atas]
            "81" -> (8, 1) [kanan bawah]
    
    Return: (x-1, y-1) untuk koordinat array 0-indexed
    """
    if len(input_str) != 2:
        return None
    
    try:
        x = int(input_str[0])
        y = int(input_str[1])
        
        if 1 <= x <= 8 and 1 <= y <= 8:
            # Konversi ke 0-indexed untuk algoritma
            # x tetap sama (1->0, 2->1, dst)
            # y dibalik (1->7, 2->6, dst karena y=1 adalah bawah)
            return (x - 1, 8 - y)
        else:
            return None
    except ValueError:
        return None

def main():
    print("=" * 50)
    print("KNIGHT'S TOUR - ALGORITMA WARNSDORFF")
    print("=" * 50)
    print("\nCara input posisi awal kuda: xy")
    print("  x = posisi horizontal (1-8, dari kiri)")
    print("  y = posisi vertikal (1-8, dari bawah)")
    print("\nContoh:")
    print("  18 = paling kiri atas")
    print("  88 = paling kanan atas")
    print("  11 = paling kiri bawah")
    print("  81 = paling kanan bawah")
    print("\nKetik 'exit' untuk keluar")
    print("=" * 50)
    
    # Tampilkan papan kosong
    display_board()
    
    # Minta input posisi awal
    user_input = input("\nMasukkan posisi awal kuda (xy): ").strip()
    
    if user_input.lower() == 'exit':
        print("Program Closed")
        return
    
    # Parse input
    position = parse_input(user_input)
    
    if position is None:
        print("Masukkan 2 angka (1-8)")
        return
    
    start_x, start_y = position
    
    # Tampilkan posisi awal
    print(f"\n Kuda dimulai dari posisi x={int(user_input[0])}, y={int(user_input[1])}")
    display_board((int(user_input[0]), int(user_input[1])))
    
    print("\n⏳ Mencari rute Knight's Tour...")
    
    # Jalankan algoritma
    success, px, py, closed = solve_knights_tour(start_x, start_y)
    
    if success:
        status = "CLOSED Tour" if closed else "OPEN Tour"
        print(f"\n Berhasil! Hasil: {status}")
        print(f"  Total langkah: {len(px) - 1}")
        
        if closed:
            print("  Kuda dapat kembali ke posisi awal!")
        else:
            print("  Kuda tidak dapat kembali ke posisi awal.")
        
        # Plotting
        print("\n📊 Menampilkan visualisasi...")
        plt.figure(figsize=(8, 8))
        
        # Plot path
        plt.plot(py, px, marker='o', linestyle='-', linewidth=2, 
                markersize=8, color='blue', alpha=0.7)
        
        # Tandai start dan end
        plt.plot(py[0], px[0], marker='s', markersize=15, 
                color='green', label='Start')
        plt.plot(py[-2] if closed else py[-1], 
                px[-2] if closed else px[-1], 
                marker='X', markersize=15, color='red', 
                label='End')
        
        # Grid Papan Catur
        plt.xticks(range(N))
        plt.yticks(range(N))
        plt.grid(True, alpha=0.3)
        plt.gca().invert_yaxis()  # Invert Y agar (0,0) di kiri atas
        plt.xlabel('Kolom (X)')
        plt.ylabel('Baris (Y)')
        plt.title(f"Knight's Tour: {status}\nStart: ({user_input[0]},{user_input[1]})")
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    else:
        print(f"\n Gagal menemukan rute dari posisi ({user_input[0]},{user_input[1]})")
        print("   Coba posisi awal yang berbeda.")

if __name__ == "__main__":
    main()
