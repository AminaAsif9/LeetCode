class Solution:
    def thousandSeparator(self, n: int) -> str:
        num_str = str(n)
        len_num_str = len(num_str)

        ret_val = ''

        i = len(num_str) - 1
        while (i >= 0):
            c = num_str[i]
            if ((len_num_str-i) % 3 != 0):
                ret_val = c + ret_val
            else:
                ret_val = '.' + c + ret_val

            i -= 1

        if (not ret_val.startswith('.')):
            return ret_val
        else:
            return ret_val[1:]