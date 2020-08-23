from flask import Blueprint, make_response

pony_api = Blueprint('pony_api', __name__)

@pony_api.route('')
def print_ponies():
    image = """
                       .::cc:::::::.
                  .::::oxxddddxxxkOdcc::.
             .:::coxxxdl:;,,,,;::cldxxkkl,,,,.
             :XXXXxcc:;,,,,,,,,,,:ccccloddddx,
             .ccxXOxxoccc:::::::::cccclloddl:;,;:::::::::.
           .:cccoxdddlccc::::::ccccccclloddc';:oOOkxxxxxxo:::cc::::.
   .:::::ccoxxddl;;,,,,;:::::::ccccllloddddc,'.:ddoccccccoxxkO0XXx:.
   .::xXOxxl;;;;;::cc:::cccclllcclldkkOOo::;''';::colccccllldOo::.
      .coxxddl:::clllcclldxxdlllldOxlloo;.....'...:docccldOO0Xxcc::.
        :KKXXxcccccccccldOKKxclookKl..............:xocclokKKXXXXXXK:
        .::::oxxxxxxxxxkOkxxdldOOxo;..............:docclldxxkk0XXx:.
             .:::::::dO0KOxxkOKNN0ddddc'..........:doccccllldkocc.
                  .,,;:cooddONX00XNWWWKkc''.......:docclldOOo:.
                  ,dd:...cxxdloddlckNNWMOcc;......:dollodOXX:
                  ,dd:...dMMl 'oooldOOXMX00o'...''cddooxO0XXx::::.                       .,,,,.
                  ,dd:...dMMl 'oo0M0oo0MMWWx,'.',,cddookKKXXKKKXX:                       ,xxdd,
                  ,xx:...dMMl 'ook0dccOMX00o'..',,cdolldxkOO0Kx::.    .,,,,,,,,,,,,,,,,,,;::;;,,.
                  ,dd:...l00: 'oolc;''xMOcc;...',,cdooolldOOOOl,,,,,,,cdl::;;;;;;;;,,,,,,.....;d,
                  ,dd:...;cc. .'';c:::lxc''...';llodxOOOkOOOdccccodl:::;'...................';,,.
                .,;::,....''...  .::::,'.....',cddxOo::::lddc,,,,cd:......,::::::::::::::ccc:,.
                ,d:..........................',cddlc.    ,xxc,:ccc:'...',,;:::::::::::::::::;,.
                ,d:..........................',cdd,      ,xxl,cdd:.....,,,'.................:d,
                .,;::::,.....................',cdd,    .,:ccccc::'....,cclc::,...........'::;,.
                  .,,,,;::::::::::::::,.......';cc:,,,,cxoccc:'....'::::::::::::;;;;;;;,,oOO;
                       .,,,,,,,,,,,cdd:.........'';:::::::::,....,:lxxc'.....';:::lddooooxOOo:.
                                   ,dd:............''''''''';:cccccc::;,;:,........,:oollllldkdc.
                                   ,dd:...........',,;;;;,,,cddddc,'..',cd:....     ,ddddlccloOX:
                                   ,dd:............',,,:lcccccoddc'.....,:::::;;,,,,:oolllllllkK:
                                 .,cdd:..............'',:ccc;';::;'........,,cdolllc::::cloooldOd::.
                            .,,,,:coddc'.................;cc;.....';::;;;;,,,,,lxxl:;,,:clooxkxdOXX:
                         .,,:cccc:,:cccc;''..............,:::::;;::lddl:ccodd, :XXxc:,,:clddOK0O0KK:
                         ,ddc,,,,,,,,,cdocc;'...............,:::::::::;';c:,,. :KKxc:,,:clddkKx:xKK:
                         ,ddc,,;;,,,,,cxdddc,'........................',cd,    :XXxc;,,:clooOX: :XX:
                       .,:cc:,,,,:cccc:,,,,:c;.....'''''''''........'',,cd,    :KKxc::::clddOX: :KK:
                       ,dc,,,,,,,cxc,,.    ,d:....;cccccccccc:,.....'';cod,    :KKkllcccclddkK: .::.
                       ,dc,,,,,;;cd,       ,d:....:dc,,,,cdddxl::,....;cod,    .ccdOdcccclookK:
                       ,dc,,,,,,,cd,       ,x:....:d,    .,,cdoccc:,...';c:,,.    cXklllclddkK:
                       ,dc,,,,,,,cd,       ,x:....:x,       ,dc,,cx:....',cxx,    .:dOOdcllldkdc.
                       ,dc;;;,,;;cd,       ,x:....:x,       ,dc,,cd:....',cxx,      :KKxccccldOXc
                       .,:ccccccc:,.    .,,;:,....:d,       ,dc,,cdl::,.',cdd,      .::oxocccldOd::::.
                         .,,,,,,,.      ,dd:....''cd,       ,dc,,:codd:.';cdd,         .:oxxxxkO0XXx:.
                                        ,dd:...',,cx,       ,dc,,,,cdd:..';cc:,.         .:::::c:::.
                                        ,dd:...',,cx,       ,xc,,,,cdd:...',,cd,
                                      .,;::,...',,cd,    .,,:l:,,,,cdd:...',,cd,
                                      ,x:......',,cd,    ,xxl,,,,,,cxx:...';;lx,
                                      ,d:......',,cd,    ,xxc,,,,:cc::,...',,cd,
                                   .,,;:,......',,cd,    ,xxoccccod:......',,cd,
                                   .,,;::::::::ccc:,.    .,,,,,,,cdl::::::ccc:,.
                                      .,,,,,,,,,,,.              .,,,,,,,,,,,.
    """
    response = make_response(image, 200)
    response.mimetype = 'text/plain'
    return response
