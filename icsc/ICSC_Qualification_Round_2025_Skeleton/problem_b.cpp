#include <iostream>
#include <vector>
#include <stdexcept>

std::vector<int> cake_calculator(int flour, int sugar) {
   /**
    * Calculates the maximum number of cakes that can be made and the leftover ingredients.
    * 
    * Args:
    *     flour: An integer larger than 0 specifying the amount of available flour.
    *     sugar: An integer larger than 0 specifying the amount of available sugar.
    *     
    * Returns:
    *     A vector of three integers: 
    *     [0] the number of cakes that can be made
    *     [1] the amount of leftover flour
    *     [2] the amount of leftover sugar  
    */
   
    // WRITE YOUR CODE HERE


}


// --- Main execution block. DO NOT MODIFY  ---
int main() {
   try {
       // 1. Read input from stdin
       std::string flour_str, sugar_str;
       std::getline(std::cin, flour_str);
       std::getline(std::cin, sugar_str);
       
       // 2. Convert inputs to appropriate types
       int flour = std::stoi(flour_str);
       int sugar = std::stoi(sugar_str);
       
       // 3. Call the cake calculator function
       std::vector<int> result = cake_calculator(flour, sugar);
       
       // 4. Print the result to stdout in the required format
       std::cout << result[0] << " " << result[1] << " " << result[2] << std::endl;
       
   } catch (const std::invalid_argument& e) {
       // Handle errors during input conversion or validation
       std::cerr << "Input Error or Validation Failed: " << e.what() << std::endl;
       return 1;
   } catch (const std::out_of_range& e) {
       // Handle out of range errors during stoi conversion
       std::cerr << "Input Error: Number out of range" << std::endl;
       return 1;
   } catch (const std::ios_base::failure& e) {
       // Handle cases where reading input failed
       std::cerr << "Error: Failed to read input" << std::endl;
       return 1;
   } catch (const std::exception& e) {
       // Catch any other unexpected errors
       std::cerr << "An unexpected error occurred: " << e.what() << std::endl;
       return 1;
   }
   
   return 0;
}