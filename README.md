# Reinforcement Learning: Q-Learning & SARSA

Proyek ini adalah program sederhana berbasis command-line untuk mendemonstrasikan dan membandingkan dua algoritma *reinforcement learning*: **Q-Learning** dan **SARSA**.

Pengguna dapat memilih jenis agen, mengatur parameter, dan melihat agen berlatih untuk menemukan jalan terbaik dalam sebuah lingkungan *grid world*.

Proyek ini dibuat untuk seleksi asisten lab AI tahun 2025.

Reinforcement Learning (Bagian 4)
[ ] Q-LEARNING
[v] SARSA

## Cara Menjalankan

**Syarat:**
* Python 3

**Langkah-langkah:**

1.  Buka terminal di dalam direktori proyek.
2.  Jalankan script utama dengan perintah:
    ```bash
    python src/main.py
    ```
3.  Program akan meminta Anda memasukkan beberapa konfigurasi secara interaktif, seperti:
    * Tipe Agen (Q-Learning/SARSA)
    * Learning Rate (`alpha`)
    * Discount Factor (`gamma`)
    * Exploration Rate (`epsilon`)
    * Jumlah episode latihan
    * Dan lain-lain.