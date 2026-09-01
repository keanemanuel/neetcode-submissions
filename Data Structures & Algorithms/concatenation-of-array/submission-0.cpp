#define pb push_back
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> a;
        for(int i=0; i< nums.size()*2; i++){
            if(i>=nums.size()){
                a.pb(nums[i-nums.size()]);
            } else{
                a.pb(nums[i]);
            }       
        }
        return a;
    }
};