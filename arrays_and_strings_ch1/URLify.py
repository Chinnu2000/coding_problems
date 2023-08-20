

def replace_spaces(url, true_length):
    format_url = ""
    for i in range(true_length):
        if url[i] != ' ':
            format_url = format_url + url[i]
        else:
            format_url = format_url + '%20'
    return format_url

if __name__ == '__main__':
    url = input()
    true_length = int(input())
    print(replace_spaces(url, true_length))