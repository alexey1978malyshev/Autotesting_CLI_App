import subprocess
# result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
# out = result.stdout
# if result.returncode == 0:
#     lst = out.split("\n")
#     if 'PRETTY_NAME="Ubuntu 24.04.1 LTS"' in lst and 'VERSION="24.04.1 LTS (Noble Numbat)"' in lst:
#         print('SUCCESS')
#     else:
#         print('FAIL')


# result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
# out = result.stdout
# if "24.04.1" in out and "Noble Numbat" in out and result.returncode == 0:
#     print('SUCCESS')
# else:
#     print('FAIL')
version_num = "24.04.1"

def check_output(command, text):
    result = subprocess.run(f"{command} /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if text in out:
        return True
    else:
        return False

if __name__ == "__main__":
    print(check_output('cat',version_num))


