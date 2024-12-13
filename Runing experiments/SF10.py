import serial
from time import sleep


class SF10():
    def __init__(self, port, name = 'UNKNOWN (SF10)'):
        '''
        port: str
            port number, e.g. COM3
        '''
        
        self.con = serial.Serial(port)
        
        print('self.con: {}'.format(self.con))
        self.name = name 
        
        print('{} at {}'.format(self.name, self.con.port))

    def __repr__(self) -> str:
        return 'Peristaltic pump (SF10)'

    def start(self, info= True):
        '''
        Starts the pump
        '''
        sleep(1)
        self.con.write(b'START\n')
        print(b'START\n')
        action = '{}:\t\tStarted.'.format(self.name)
        if info:
            print(action)

    def stop(self, info = True):
        '''
        stops the pump
        '''
        self.con.write(b'STOP\n')
        
        action = '{}:\t\tStopped.'.format(self.name)
        if info:
            print(action)

    def changeFlowrate(self, flowrate, start = True, info = True):
        '''
        flowrate: float
            flowrate in ml/min
        '''
        command = 'SETFLOW {}\n'.format(flowrate)
        self.con.write(bytes(str(command), 'utf8'))

        action = '{}:\t\tFlowrate changed to {} mL/min'.format(self.name, flowrate)
        if info:
            print(action)
        if start:
            self.start()


