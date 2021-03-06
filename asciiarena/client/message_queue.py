from common.package_queue import PackageQueue, InputPack, OutputPack
import queue

class ReceiveMessageError(Exception):
    pass

class MessageQueue(PackageQueue):

    def __init__(self):
        PackageQueue.__init__(self)

    def _attach_endpoint(self, endpoint):
        self._endpoint = endpoint

    def _receive_message(self, message_class_list):
        while True:
            input_pack = self._input_queue.get()
            if None != input_pack.message:
                for message_class in message_class_list:
                    if message_class == input_pack.message.__class__:
                        return input_pack.message
            else:
                raise ReceiveMessageError()

    def _send_message(self, message):
        self._output_queue.put(OutputPack(message, self._endpoint))

    def _end_communication(self):
        self._output_queue.put(OutputPack(None, self._endpoint))

