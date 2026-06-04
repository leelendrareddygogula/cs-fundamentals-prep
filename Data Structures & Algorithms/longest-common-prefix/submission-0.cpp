class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string check = strs[0];
        string res = "";
        for(int i = 0 ; i < check.size() ; i++)
        {
            for(auto str : strs)
            {
                if(i == str.size() or str[i] != check[i])
                {
                    return res;
                }
                
            }
            res += check[i];
        }
        return res;
    }
};