import pytest
from core.parser import HTMLParser

def test_parser_extracts_vehicles():
    html = """
   <div class="car col-xs-6 col-sm-4 col-lg-3 col-centered ng-scope" data-ng-repeat="np in nameplategroups[1] | orderBy:'price' track by $index">

        <!-- ngIf: ::(!main.isYese && !np.performance) --><a data-ng-if="::(!main.isYese &amp;&amp; !np.performance)" class="vehicle-box acc-linktype ng-scope" aria-label="cliquez pour voir la page d'équipement du  Bronco® 2025" data-ng-click="main.switchViewToNewSearchInventory($event, 'nameplate', np, np.thumb)" acc-link="" tabindex="0">
            <!-- ngIf: ::!np.thumb --><div data-ng-if="::!np.thumb" class="ng-scope">
                <!-- ngIf: ::main.prm.linktype && main.prm.flag !== 'new-search-inventory' || np.isVftEnabled --><div class="wrapper ng-scope ng-isolate-scope" style="display: none;;display: none;" data-ng-if="::main.prm.linktype &amp;&amp; main.prm.flag !== 'new-search-inventory' || np.isVftEnabled" data-link-item="[np, null]"><div data-ng-click="close($event);" class="box box-1" tabindex="0"><span class="icon-closer"></span></div><!-- ngRepeat: link in links --></div><!-- end ngIf: ::main.prm.linktype && main.prm.flag !== 'new-search-inventory' || np.isVftEnabled -->
            </div><!-- end ngIf: ::!np.thumb -->

            <!-- ngIf: ::main.make === 'Lincoln' -->
            <!-- ngIf: ::main.make === 'Ford' --><div class="vehicle-img-wrap ng-scope" data-ng-if="::main.make === 'Ford'">
                <!-- ngIf: ::!np.thumb --><img data-ng-if="::!np.thumb" class="vehicle-img img-responsive vehicle-img-hover-hide  ng-scope ng-isolate-scope lazyloaded" data-ng-lazy-src="//buildfoc.ford.com/dig/Ford/Bronco/2025/HD-THUMB/Image%5B%7CFord%7CBronco%7C2025%7C1%7C1.%7C101A.E6A..PT9..88L.89V.43L.572.B3NAB.87B.60B.2DR.64A.TDT.ESO.X4L.EGJAE.99H.ICDAW.58Z.ICPAE.IDBAL.IEVAQ.94B.77A.44Q.CLO.%5D/EXT/5/vehicle.png" ng-lazy-src-group="SUVs &amp; Crossovers" alt="" data-src="//buildfoc.ford.com/dig/Ford/Bronco/2025/HD-THUMB/Image%5B%7CFord%7CBronco%7C2025%7C1%7C1.%7C101A.E6A..PT9..88L.89V.43L.572.B3NAB.87B.60B.2DR.64A.TDT.ESO.X4L.EGJAE.99H.ICDAW.58Z.ICPAE.IDBAL.IEVAQ.94B.77A.44Q.CLO.%5D/EXT/5/vehicle.png" fetchpriority="high" src="//buildfoc.ford.com/dig/Ford/Bronco/2025/HD-THUMB/Image%5B%7CFord%7CBronco%7C2025%7C1%7C1.%7C101A.E6A..PT9..88L.89V.43L.572.B3NAB.87B.60B.2DR.64A.TDT.ESO.X4L.EGJAE.99H.ICDAW.58Z.ICPAE.IDBAL.IEVAQ.94B.77A.44Q.CLO.%5D/EXT/5/vehicle.png"><!-- end ngIf: ::!np.thumb -->
                <!-- ngIf: ::np.thumb -->
            </div><!-- end ngIf: ::main.make === 'Ford' -->

            <div class="vehicle-title">
                <div class="veh-year-desc-wrap">
                    <strong class="np-desc ng-binding" data-ng-bind-template="BRONCO®">BRONCO®</strong>
                    <span class="np-year ng-binding" data-ng-bind-template="2025">2025</span>
                    <!-- ngIf: ::(main.region === 'CA' && np.desc == 'Focus Electric') -->
                </div>
            </div>

            <div class="vehicle-info-wrap">
                <!-- ngIf: ::!np.thumb --><div data-ng-if="::!np.thumb" class="price-box ng-scope">
                    <span class="msrp">
                                <!-- From $  -->
                                <span data-ng-bind-html="::np.priceLabel" class="ng-binding">À partir de</span>
                                <span style="font-size: 25%;">&nbsp;</span>
                                <span>48&nbsp;260&nbsp;$</span>
                                    <span class="dollar-amt ng-binding" data-ng-bind="::np.price | number:0">$</span>
                                <sup data-uniqid="2_1" data-ng-click="main.disclaimerTooltip($event, this, main.discStartingMsrp, main.discStartingMsrpText)" data-ng-bind="::main.discStartingMsrp" class="vehicle-title-disclosure ng-binding ng-isolate-scope" acc-action-item="" aria-haspopup="dialog" aria-label="1 avis légal" role="button" tabindex="0">1</sup>
                            </span>
                </div><!-- end ngIf: ::!np.thumb -->

                <!-- ngIf: ::(np.spec.mpgCity && np.spec.mpgHwy && main.region === 'US') -->

                <!-- ngIf: ::(np.spec.l100kmCity && np.spec.l100kmHwy && main.region === 'CA') -->

                <!-- ngIf: ::!np.thumb --><div data-ng-if="::!np.thumb" class="ng-scope">
                    <!-- ngIf: ::main.isYese -->
                    <!-- ngIf: ::np.spec.gvwr -->
                </div><!-- end ngIf: ::!np.thumb -->
            </div>
        </a><!-- end ngIf: ::(!main.isYese && !np.performance) -->

        <!-- ngIf: ::(!main.isYese && np.performance) -->

    </div>
    """
    parser = HTMLParser(html)
    vehicles = parser.parse_vehicles()
    assert len(vehicles) == 1
    assert "Bronco" in vehicles[0].name.capitalize()

def test_parser_with_empty_html():
    parser = HTMLParser("")
    vehicles = parser.parse_vehicles()
    assert vehicles == []