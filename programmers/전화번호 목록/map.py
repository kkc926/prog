class Solution {
    public boolean solution(String[] phone_book) {
        for (int i = 0; i < phone_book.length; i++) {
            String prefix = phone_book[i];
            for (int j = i + 1; j < phone_book.length; j++) {
                String target = phone_book[j];
                if (target.length() > prefix.length()) {
                    if (target.startsWith(prefix)) {
                        return false;
                    }
                } else {
                    if (prefix.startsWith(target)) {
                        return false;
                    }
                }
            }
        }
        
        return true;
    }
}