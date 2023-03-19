def get_cities():
    cities = ["56.4611,-2.97702", "59.88369,-1.30316", "60.33047,-1.22484", "60.15232,-1.16779", "55.39766,-2.77533", "55.47531,-2.54111", "55.53631,-2.87156", "55.58238,-2.6933", "55.58723,-2.41571", "55.64182,-2.67051", "55.70073,-2.57127", "55.733,-2.7533", "55.74699,-2.01275", "55.86735,-2.12305", "55.92975,-2.36975", "55.65331,-2.2384", "55.78792,-2.31578", "55.71203,-2.44887", "55.6239,-2.80997", "56.65112,-3.69152", "56.56249,-3.59805", "56.37332,-3.82657", "56.37162,-3.99491", "56.71451,-4.96427", "56.32927,-3.8277", "56.675,-5.10977", "57.05693,-6.50319", "57.01529,-6.28049", "56.90217,-6.14094", "57.00374,-5.83251", "56.96381,-5.7856", "56.26072,-3.78244", "56.91265,-5.84124", "56.84536,-5.74736", "56.72124,-5.86584", "57.07578,-4.93032", "56.92574,-4.92676", "56.82148,-5.11207", "57.14424,-4.68275", "56.89234,-4.81575", "56.79185,-4.6002", "56.30228,-3.70355", "57.3298,-3.60464", "57.26187,-3.64646", "57.25419,-3.74891", "57.28761,-3.80028", "57.19857,-3.80587", "57.08834,-4.02169", "57.05377,-4.15504", "56.38691,-3.40439", "56.93428,-4.255", "56.7741,-3.88855", "56.68745,-4.3823", "56.70697,-3.81003", "56.60974,-3.94063", "56.45299,-3.18614", "56.53749,-3.27335", "56.57551,-3.15253", "56.63942,-3.23438", "56.60845,-3.36046", "56.42113,-3.47537", "55.80948,-4.55184", "55.9014,-4.45228", "56.62454,-6.54449", "56.49469,-6.8835", "56.33403,-6.39324", "56.61228,-6.12216", "56.53313,-6.22911", "56.49693,-6.18279", "56.51761,-5.96381", "56.48108,-5.98112", "56.36426,-6.03373", "55.90944,-4.49919", "56.38044,-6.08894", "56.43624,-6.14202", "56.31356,-6.23228", "56.32913,-6.35382", "56.46916,-5.72805", "56.43838,-5.67471", "56.38234,-5.71469", "56.35932,-5.85014", "56.07177,-6.20088", "55.87979,-5.91287", "55.86377,-4.53462", "55.83105,-4.50854", "55.7826,-6.39313", "55.73797,-6.38332", "55.68236,-6.50288", "55.86226,-6.11902", "55.81932,-6.1656", "55.79785,-6.29265", "55.7559,-6.28324", "55.63962,-6.18624", "55.6747,-5.74115", "55.87464,-4.39623", "56.59186,-5.33433", "56.46816,-5.38681", "56.52032,-4.77019", "56.40507,-5.22391", "56.4021,-5.49931", "56.36978,-5.05569", "56.20284,-5.11658", "56.05245,-5.46273", "56.0133,-5.44799", "55.85205,-4.44757", "55.80476,-5.47741", "55.43603,-5.60305", "56.15422,-5.08365", "56.25758,-4.9369", "56.21553,-5.04017", "56.15675,-4.90504", "55.95474,-4.93154", "55.97074,-5.1572", "55.90186,-5.24762", "55.83482,-5.0567", "55.82896,-4.43334", "55.9528,-4.82244", "55.88928,-4.88661", "55.86512,-4.88162", "55.94351,-4.79613", "55.94279,-4.74802", "55.92757,-4.66368", "55.89235,-4.62927", "55.7954,-4.62273", "55.85649,-4.5821", "55.83375,-4.55184", "55.84457,-4.41674", "55.72496,-3.96658", "55.7305,-3.84103", "55.83008,-3.79303", "55.86704,-3.96257", "55.85964,-4.03091", "55.81846,-4.02078", "55.77028,-4.05337", "55.77706,-3.91179", "55.56677,-3.59544", "55.66661,-3.78555", "55.68013,-4.06932", "55.79943,-3.97512", "56.20965,-2.83356", "56.19755,-3.01061", "56.19719,-3.15405", "56.19678,-3.19756", "56.14548,-3.29416", "56.11421,-3.36066", "56.06346,-3.23037", "56.12234,-3.18238", "56.34184,-2.81865", "56.30055,-3.0505", "56.31048,-3.23992", "56.20866,-3.43173", "56.07674,-3.49272", "56.0471,-3.4145", "56.23024,-2.70011", "56.12815,-3.1375", "58.0137,-3.85692", "58.11611,-3.6636", "58.18641,-3.50018", "58.24908,-3.44148", "58.28747,-3.38163", "58.30741,-3.27829", "58.34893,-3.16359", "59.04195,-3.00217", "58.95963,-3.27278", "58.9803,-2.95862", "58.58913,-3.55523", "58.45518,-3.89556", "58.50634,-3.49149", "58.30505,-4.12991", "57.97509,-3.975", "58.45801,-3.12092", "55.49734,-4.60446", "55.4711,-4.61222", "55.44739,-4.62805", "55.41582,-4.50427", "55.50987,-4.38668", "55.59894,-4.38256", "55.79725,-4.86224", "55.64435,-4.49499", "55.75701,-4.85291", "55.75447,-4.92287", "55.5388,-5.17162", "55.21894,-4.83313", "55.75263,-4.6884", "55.70981,-4.71412", "55.69135,-4.85449", "55.65019,-4.80697", "55.64176,-4.78253", "55.64157,-4.75072", "55.59619,-4.56338", "55.34585,-4.66707", "55.45063,-4.23917", "55.61075,-4.28164", "55.60713,-4.33065", "55.74859,-4.62596", "55.74041,-4.67162", "55.6553,-4.69921", "55.61923,-4.66337", "55.61736,-4.62512", "55.54945,-4.64755", "55.5958,-4.49509", "57.56922,-4.17706", "57.55419,-4.26477", "57.58435,-4.38376", "57.32228,-4.50465", "57.52634,-4.45682", "57.36636,-6.4279", "57.45873,-6.611", "57.43101,-5.61538", "57.34465,-5.55367", "57.33737,-5.65106", "57.48055,-6.24636", "57.4679,-4.4112", "57.2277,-5.94693", "57.31102,-6.09713", "57.29467,-6.34284", "57.1141,-5.98441", "57.06714,-5.90508", "57.11488,-5.87374", "57.1555,-5.81015", "57.23946,-5.82877", "57.27372,-5.73605", "57.27446,-5.64981", "57.44843,-4.53328", "57.61104,-3.60363", "57.63161,-3.11041", "57.71706,-3.28931", "57.65468,-3.32732", "57.47726,-4.24499", "58.01527,-4.15668", "58.27684,-4.80032", "57.91578,-5.17243", "57.89135,-4.04295", "57.89133,-4.35512", "57.77322,-5.01018", "57.74156,-5.50682", "57.72377,-5.72019", "57.78653,-3.90748", "57.46833,-4.19107", "57.80478,-4.06162", "57.70169,-4.15479", "57.69985,-4.26043", "57.66431,-4.33703", "57.59965,-4.42996", "57.58564,-4.54783", "57.3428,-4.01239", "57.57422,-3.86458", "57.67758,-4.03762", "57.58536,-4.12616", "57.4874,-4.23059", "56.97148,-7.47153", "57.23253,-7.34593", "57.44703,-7.33888", "57.6008,-7.29943", "57.79992,-6.96123", "57.86961,-6.69056", "57.87876,-6.85387", "58.24916,-6.46768", "58.21347,-6.38138", "56.0137,-4.75306", "56.01196,-4.58444", "55.95195,-4.57403", "55.91309,-4.4066", "55.79259,-4.40873", "55.77345,-4.32941", "55.77811,-4.27227", "55.76912,-4.17289", "55.81977,-4.20605", "55.80406,-4.12856", "55.8221,-4.07206", "55.87372,-4.10199", "55.95345,-4.01019", "55.94755,-3.98586", "55.94024,-4.15364", "55.97334,-4.0577", "55.91127,-4.21604", "56.04243,-4.36487", "55.94261,-4.32034", "55.91905,-4.33014", "55.92205,-4.45358", "55.82157,-4.35145", "55.8477,-4.34823", "55.85734,-4.31365", "55.84769,-4.25237", "55.80446,-4.30573", "55.80494,-4.23074", "55.81438,-4.25523", "55.81825,-4.28898", "55.83234,-4.25627", "55.83815,-4.28216", "55.84824,-4.22204", "55.86837,-4.25196", "55.86817,-4.11128", "55.87351,-4.16593", "55.8484,-4.16293", "55.85748,-4.20819", "55.86619,-4.27262", "55.90193,-4.28431", "55.88998,-4.25002", "55.88063,-4.22069", "55.8858,-4.28176", "55.86382,-4.2549", "55.9094,-4.36476", "55.88095,-4.34864", "55.89358,-4.3462", "55.88006,-4.30061", "55.87356,-4.31142", "55.86038,-4.24671", "56.14242,-3.93955", "56.13075,-4.05001", "56.09695,-3.91636", "56.02149,-3.91423", "56.02564,-3.81814", "55.99734,-3.90662", "56.01087,-3.71958", "56.46574,-4.31969", "56.4065,-4.63059", "56.00499,-3.75461", "56.37057,-4.3139", "56.32448,-4.32728", "56.24019,-4.21887", "56.19081,-4.05966", "56.20249,-3.94903", "56.16536,-3.66044", "56.15078,-3.74032", "56.15263,-3.79998", "56.15009,-3.84977", "56.11516,-3.78053", "55.98555,-3.79381", "55.9336,-3.18463", "55.94909,-3.16268", "55.96075,-3.16463", "55.97144,-3.17456", "55.84748,-3.57178", "55.89212,-3.524", "55.8936,-3.47608", "55.93756,-3.48256", "56.01153,-3.6041", "55.97463,-3.21633", "55.97656,-3.59785", "55.9011,-3.66353", "55.85976,-3.66336", "55.73689,-3.3491", "55.65494,-3.19209", "55.62015,-3.06558", "55.62422,-3.0101", "55.99389,-2.52428", "55.94854,-2.7751", "55.99057,-2.6557", "55.96253,-3.25761", "56.04766,-2.73052", "55.78638,-2.96006", "55.86188,-2.95873", "55.85637,-2.85155", "55.91053,-2.94233", "55.90919,-2.8799", "55.94196,-2.94469", "55.96799,-2.94853", "56.03627,-2.82661", "55.98455,-3.38336", "55.95412,-3.19967", "55.95652,-3.39838", "55.9306,-3.38624", "55.89063,-3.42319", "55.83257,-3.22307", "55.85821,-3.17434", "55.85051,-3.13257", "55.83956,-3.05081", "55.88441,-3.06001", "55.93845,-3.04548", "55.87905,-3.15579", "55.95417,-3.19486", "55.87324,-3.10446", "55.87667,-3.12215", "55.90704,-3.14222", "55.92221,-3.15387", "55.94686,-3.11136", "55.90925,-3.28308", "55.90788,-3.24144", "55.94262,-3.27137", "55.93387,-3.24867", "55.92077,-3.20984", "55.95243,-3.1884", "54.87815,-5.02123", "54.87259,-4.51567", "54.96738,-4.01219", "54.83721,-4.05555", "54.92201,-3.81016", "55.37555,-3.95236", "55.23678,-3.79927", "55.06442,-3.65683", "54.99731,-3.06777", "55.08069,-2.98539", "55.17291,-3.02849", "54.98928,-3.25044", "55.11331,-3.33584", "55.31977,-3.43735", "55.07353,-3.58045", "56.74798,-2.6672", "56.6565,-2.92171", "56.5033,-2.71814", "56.43723,-2.92612", "56.47812,-2.86217", "56.48209,-2.93534", "56.48257,-2.98894", "56.46968,-3.02756", "56.57312,-2.59738", "56.74724,-2.4268", "56.4611,-2.97702", "57.67442,-2.92559", "57.5239,-2.99024", "57.45361,-2.76333", "57.52537,-2.3941", "57.34396,-2.60651", "57.28907,-2.40485", "57.65139,-2.56639", "57.66877,-2.49122", "57.65714,-2.04358", "57.50079,-1.88819", "57.37592,-2.10478", "56.97778,-2.21718", "57.48589,-3.2261", "57.33098,-3.35051", "57.19715,-3.06589", "57.03829,-3.14869", "57.09393,-2.81204", "57.22464,-2.74203", "57.15545,-2.31742", "57.07479,-2.52623", "56.84678,-2.47712", "57.15311,-2.11241", "57.16284,-2.11228", "57.21242,-2.08776", "57.18724,-2.11913", "57.2096,-2.20033", "57.16115,-2.15543", "57.13868,-2.16525", "57.10076,-2.27073", "57.10801,-2.23776", "57.101,-2.1106", "57.13875,-2.09089", "57.13514,-2.11731"]
    return cities
# Provide Location Input For API request