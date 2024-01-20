from concurrent import futures

import grpc
import meterservice_pb2
import meterservice_pb2_grpc

# new versions of grpc-tools creates a less explicit pb2.py file
class MeterReadingService(meterservice_pb2_grpc.MeterReadingServiceServicer):
    def AddReading(self, reading_packet, context):
        readings = reading_packet.Readings
        status = reading_packet.Successful

        print(f'status is {status}')

        for read in readings:
            print(read.CustomerId)
            print(read.ReadingValue)
            print(read.Notes)
            print(read.ReadingTime)

        status_message = meterservice_pb2.StatusMessage()
        status_message.Success = meterservice_pb2.ReadingStatus.Success
        status_message.Message = 'Everything is OK'
        return status_message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meterservice_pb2_grpc.add_MeterReadingServiceServicer_to_server(MeterReadingService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
