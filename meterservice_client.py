from concurrent import futures
import time

import grpc
import meterservice_pb2
import meterservice_pb2_grpc
from meterservice_pb2 import ReadingPacket, ReadingStatus, ReadingMessage


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        packet = ReadingPacket(Successful = ReadingStatus.Success)
        reading = ReadingMessage(CustomerId = 1, ReadingTime = 'now', ReadingValue = 100)
        packet.Readings.append(reading)
        stub = meterservice_pb2_grpc.MeterReadingServiceStub(channel)
        response = stub.AddReading(packet)
        print(response)


if __name__ == '__main__':
    run()