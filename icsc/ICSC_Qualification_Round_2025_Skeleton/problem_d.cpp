#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <stdexcept>
#include <sstream>

/**
 * Generate a 10x10 word search puzzle containing the given words.
 * 
 * @param words A vector of strings to include in the puzzle.
 * @return A 2D vector of chars representing the word search puzzle.
 */
std::vector<std::vector<char>> create_crossword(const std::vector<std::string>& words) {

    // WRITE YOUR CODE HERE

}



// --- Main execution block. DO NOT MODIFY.  ---
int main() {
    try {
        // Seed random number generator
        std::srand(static_cast<unsigned int>(std::time(nullptr)));
        
        // Read words from first line (comma-separated)
        std::string wordsInput;
        std::getline(std::cin, wordsInput);
        
        std::vector<std::string> words;
        std::stringstream ss(wordsInput);
        std::string word;
        
        // Parse comma-separated words
        while (std::getline(ss, word, ',')) {
            // Trim whitespace
            word.erase(0, word.find_first_not_of(" \t\r\n"));
            word.erase(word.find_last_not_of(" \t\r\n") + 1);
            
            if (!word.empty()) {
                words.push_back(word);
            }
        }
        
        // Generate the word search puzzle
        std::vector<std::vector<char>> puzzle = create_crossword(words);
        
        // Print the result as a 2D grid
        for (const auto& row : puzzle) {
            for (char c : row) {
                std::cout << c;
            }
            std::cout << std::endl;
        }
        
    } catch (const std::runtime_error& e) {
        std::cerr << "Input Error: " << e.what() << std::endl;
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "An unexpected error occurred: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}