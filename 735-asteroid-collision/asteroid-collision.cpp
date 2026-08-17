class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        for (int i : asteroids) {
            bool alive = true;
            while (alive && i < 0 && !stack.empty() && stack.back() > 0) {
                if (stack.back() < abs(i)) {
                    stack.pop_back();
                }
                else if (stack.back() == abs(i)) {
                    stack.pop_back();
                    alive = false;
                }
                else {
                    alive = false;
                }
            }
            if (alive) {
                stack.push_back(i);
            }
        }
        return stack;
    }
};