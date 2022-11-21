# #   Created by Elshad Karimov on 31/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# # How to use multiprocessing.Queue as a FIFO queue:
#
# ____ multiprocessing ______ Queue
#
# customQueue _ Queue(maxsize_ 3)
# customQueue.put(1)
# print(customQueue.get())