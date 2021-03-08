# import threading
import concurrent.futures


# Create threads
def create_threads(ip_list, ssh_conn_func):

    # New and efficient way of doing threading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(ssh_conn_func, ip_list)

    # Old way of doing threading
    # threads = list()
    #
    # for ip in ip_list:
    #     th = threading.Thread(target=ssh_conn_func, args=(ip,))  # args is a tuple with single element
    #     th.start()
    #     threads.append(th)
    #
    # for thread in threads:
    #     thread.join()
