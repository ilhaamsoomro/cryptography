# Cryptography Algorithms

This repository contains implementations of various classical cryptography algorithms in Python. These algorithms are often used for encryption and decryption of messages.

## Algorithms Included:

### 1. Vigenère Cipher:
The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. The algorithm uses a keyword to shift each letter of the plaintext by a different amount, creating a repeating key. The encrypted message is produced by shifting each plaintext letter according to the corresponding letter in the keyword.

### 2. Vernam Cipher:
The Vernam cipher, also known as the one-time pad, is a method of encrypting plaintext with a random key that is as long as the plaintext itself. Each letter of the plaintext is combined with the corresponding letter of the key using modular addition. The key should only be used once and must be kept completely secret.

### 3. Morse Code:
Morse code is a method used in telecommunication to encode text characters as sequences of two different signal durations, called dots and dashes or dits and dahs. This implementation provides functions for encoding and decoding text messages using Morse code.

### 4. Caesar Cipher:
The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet. In this implementation, the shift value is configurable.

### 5. Playfair Cipher:
The Playfair cipher is a manual symmetric encryption technique and was the first literal digraph substitution cipher. The algorithm encrypts pairs of letters instead of single letters, which makes it more resistant to frequency analysis attacks. It uses a 5x5 grid of letters constructed from a keyword to perform the encryption and decryption operations.

## Contribution:
Contributions to this repository are welcome. If you have improvements or additional algorithms you'd like to add, feel free to create a pull request.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
