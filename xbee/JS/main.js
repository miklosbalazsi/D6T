/**
 *
 */

const SerialPort = require('serialport');
const xbee_api = require('xbee-api');
const C = xbee_api.constants;
const xbeeAPI = new xbee_api.XBeeAPI( { api_mode: 1 } );

const serialport = new SerialPort("/dev/ttyUSB0", {
  baudRate: 9600,
});

const Coord = null;

/*
 * find out Corrdinator Serial port 
 * { manufacturer: 'FTDI',
 *   serialNumber: 'AK05ZJ6L',
 *   pnpId: 'usb-FTDI_FT232R_USB_UART_AK05ZJ6L-if00-port0',
 *   locationId: undefined,
 *   vendorId: '0403',
 *   productId: '6001',
 *   comName: '/dev/ttyUSB2' },
 */
/*
SerialPort.list().then( function(list){


  var CE_command = { // AT Request to be sent
    type: C.FRAME_TYPE.AT_COMMAND,
    command: "CE",
    commandParameter: [],
  };
  const ATCE = xbeeAPI.buildFrame(CE_command);

	for (var i=0 ; i<list.length ; i++){
		var ser = list[i];
		var vendorProduct = ser.vendorId + ser.productId;
		if ( "04036001" ==  vendorProduct ){
		  console.log( ser.comName );
		  var Port = new SerialPort( ser.comName , { baudRate: 9600 });			  	
	          Port.write(ATCE)
		    .catch()
                    .then(function(){console.log(Port.read())});		
		}		
	}	
 } );
*/
serialport.pipe(xbeeAPI.parser);
xbeeAPI.builder.pipe(serialport);
 
serialport.on("open", function() {
  var frame_obj = { // AT Request to be sent
    type: C.FRAME_TYPE.AT_COMMAND,
    command: "SM",
    commandParameter: [],
  };

  	 
  console.log("<<",xbeeAPI.buildFrame(frame_obj) );
  xbeeAPI.builder.write(frame_obj);
});
 
// All frames parsed by the XBee will be emitted here
xbeeAPI.parser.on("data", function(frame) {
  console.log(">>", frame);
  console.log(frame.commandData);	
});

