class wall():
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def show(self):
        stroke(0)
        strokeWeight(2)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
        
class checkpoint():
    
    def __init__(self, start, end, id):
        self.start = start
        self.end = end
        self.id = id
        
    def show(self):
        stroke(255, 0, 255)
        strokeWeight(2)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
        
class finishLine():
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def show(self):
        stroke(0,230,0)
        strokeWeight(2)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
        
class CoordinatesData():
    
    def __init__(self):
        self.finishLines = [(PVector(346.0, 717.0), PVector(374.0, 653.0)),
                            (PVector(371.0, 741.0), PVector(401.0, 678.0))]
        
        self.walls = [(PVector(356.0, 727.0), PVector(131.0, 572.0)),
                      (PVector(131.0, 572.0), PVector(208.0, 281.0)),
                      (PVector(208.0, 281.0), PVector(312.0, 88.0)),
                      (PVector(312.0, 88.0), PVector(600.0, 125.0)),
                      (PVector(600.0, 125.0), PVector(839.0, 95.0)),
                      (PVector(839.0, 95.0), PVector(886.0, 262.0)),
                      (PVector(886.0, 262.0), PVector(734.0, 433.0)),
                      (PVector(734.0, 433.0), PVector(879.0, 660.0)),
                      (PVector(879.0, 660.0), PVector(662.0, 804.0)),
                      (PVector(662.0, 804.0), PVector(404.0, 759.0)),
                      (PVector(404.0, 759.0), PVector(356.0, 727.0)),
                      (PVector(384.0, 663.0), PVector(256.0, 529.0)),
                      (PVector(256.0, 529.0), PVector(273.0, 302.0)),
                      (PVector(273.0, 302.0), PVector(378.0, 162.0)),
                      (PVector(378.0, 162.0), PVector(537.0, 199.0)),
                      (PVector(537.0, 199.0), PVector(748.0, 157.0)),
                      (PVector(748.0, 157.0), PVector(775.0, 257.0)),
                      (PVector(775.0, 257.0), PVector(634.0, 415.0)),
                      (PVector(634.0, 415.0), PVector(689.0, 576.0)),
                      (PVector(689.0, 576.0), PVector(757.0, 637.0)),
                      (PVector(757.0, 637.0), PVector(624.0, 700.0)),
                      (PVector(624.0, 700.0), PVector(440.0, 675.0)),
                      (PVector(440.0, 675.0), PVector(384.0, 663.0))]
        
        self.checkpoints = [(PVector(131.0, 572.0), PVector(256.0, 529.0), 0),
                            (PVector(208.0, 281.0), PVector(273.0, 302.0), 1),
                            (PVector(312.0, 88.0), PVector(378.0, 162.0), 2),
                            (PVector(600.0, 125.0), PVector(537.0, 199.0), 3),
                            (PVector(839.0, 95.0), PVector(748.0, 157.0), 4),
                            (PVector(886.0, 262.0), PVector(775.0, 257.0), 5),
                            (PVector(734.0, 433.0), PVector(634.0, 415.0), 6),
                            (PVector(879.0, 660.0), PVector(757.0, 637.0), 7),
                            (PVector(662.0, 804.0), PVector(624.0, 700.0), 8),
                            (PVector(430.0, 763.0), PVector(456, 676), 9),
                            (PVector(491.0, 773.0), PVector(514, 685), 10),
                            (PVector(569.0, 787.0), PVector(573, 692), 11),
                            (PVector(719.0, 765.0), PVector(677, 674), 12),
                            (PVector(786.0, 721.0), PVector(723, 655), 13),
                            (PVector(727.0, 609.0), PVector(840, 599), 14),
                            (PVector(795.0, 527.0), PVector(684, 561), 15),
                            (PVector(664.0, 502.0), PVector(762, 475), 16),
                            (PVector(698.0, 343.0), PVector(765, 396), 17),
                            (PVector(742.0, 295.0), PVector(818, 337), 18),
                            (PVector(763.0, 213.0), PVector(860, 171), 19),
                            (PVector(678.0, 170.0), PVector(729, 108), 20),
                            (PVector(608.0, 184.0), PVector(650, 118), 21),
                            (PVector(493.0, 188.0), PVector(519, 114), 22),
                            (PVector(435.0, 174.0), PVector(430, 103), 23),
                            (PVector(346.0, 203.0), PVector(277, 152), 24),
                            (PVector(307.0, 255.0), PVector(242, 218), 25),
                            (PVector(268.0, 355.0), PVector(190, 347), 26),
                            (PVector(175.0, 405.0), PVector(264, 409), 27),
                            (PVector(161.0, 456.0), PVector(260, 462), 28),
                            (PVector(147.0, 509.0), PVector(258, 493), 29),
                            (PVector(195.0, 615.0), PVector(280, 553), 30),
                            (PVector(247.0, 651.0), PVector(311, 586), 31),
                            (PVector(301.0, 688.0), PVector(352, 629), 32)]
        
        self.walls2 = [(PVector(404.0, 763.0), PVector(478.0, 784.0)),
                       (PVector(478.0, 784.0), PVector(548.0, 790.0)),
                       (PVector(548.0, 790.0), PVector(646.0, 798.0)),
                       (PVector(646.0, 798.0), PVector(700.0, 823.0)),
                       (PVector(700.0, 823.0), PVector(788.0, 843.0)),
                       (PVector(788.0, 843.0), PVector(852.0, 823.0)),
                       (PVector(852.0, 823.0), PVector(905.0, 780.0)),
                       (PVector(905.0, 780.0), PVector(933.0, 716.0)),
                       (PVector(933.0, 716.0), PVector(935.0, 647.0)),
                       (PVector(935.0, 647.0), PVector(898.0, 591.0)),
                       (PVector(898.0, 591.0), PVector(851.0, 537.0)),
                       (PVector(851.0, 537.0), PVector(826.0, 475.0)),
                       (PVector(826.0, 475.0), PVector(826.0, 434.0)),
                       (PVector(826.0, 434.0), PVector(848.0, 382.0)),
                       (PVector(848.0, 382.0), PVector(878.0, 351.0)),
                       (PVector(878.0, 351.0), PVector(914.0, 319.0)),
                       (PVector(914.0, 319.0), PVector(945.0, 269.0)),
                       (PVector(945.0, 269.0), PVector(949.0, 202.0)),
                       (PVector(949.0, 202.0), PVector(923.0, 153.0)),
                       (PVector(923.0, 153.0), PVector(875.0, 115.0)),
                       (PVector(875.0, 115.0), PVector(804.0, 93.0)),
                       (PVector(804.0, 93.0), PVector(737.0, 84.0)),
                       (PVector(737.0, 84.0), PVector(638.0, 98.0)),
                       (PVector(638.0, 98.0), PVector(564.0, 88.0)),
                       (PVector(564.0, 88.0), PVector(477.0, 93.0)),
                       (PVector(477.0, 93.0), PVector(398.0, 129.0)),
                       (PVector(398.0, 129.0), PVector(296.0, 143.0)),
                       (PVector(296.0, 143.0), PVector(218.0, 136.0)),
                       (PVector(218.0, 136.0), PVector(141.0, 156.0)),
                       (PVector(141.0, 156.0), PVector(101.0, 203.0)),
                       (PVector(101.0, 203.0), PVector(96.0, 263.0)),
                       (PVector(96.0, 263.0), PVector(115.0, 320.0)),
                       (PVector(115.0, 320.0), PVector(125.0, 371.0)),
                       (PVector(125.0, 371.0), PVector(117.0, 412.0)),
                       (PVector(117.0, 412.0), PVector(82.0, 440.0)),
                       (PVector(82.0, 440.0), PVector(57.0, 478.0)),
                       (PVector(57.0, 478.0), PVector(57.0, 499.0)),
                       (PVector(57.0, 499.0), PVector(61.0, 548.0)),
                       (PVector(61.0, 548.0), PVector(85.0, 600.0)),
                       (PVector(85.0, 600.0), PVector(114.0, 622.0)),
                       (PVector(114.0, 622.0), PVector(176.0, 624.0)),
                       (PVector(176.0, 624.0), PVector(237.0, 629.0)),
                       (PVector(237.0, 629.0), PVector(287.0, 651.0)),
                       (PVector(287.0, 651.0), PVector(325.0, 690.0)),
                       (PVector(325.0, 690.0), PVector(352.0, 729.0)),
                       (PVector(352.0, 729.0), PVector(404.0, 763.0)),
                       ## Inner
                       (PVector(433.0, 695.0), PVector(506.0, 723.0)),
                       (PVector(506.0, 723.0), PVector(565.0, 733.0)),
                       (PVector(565.0, 733.0), PVector(609.0, 733.0)),
                       (PVector(609.0, 733.0), PVector(682.0, 736.0)),
                       (PVector(682.0, 736.0), PVector(740.0, 699.0)),
                       (PVector(740.0, 699.0), PVector(787.0, 655.0)),
                       (PVector(787.0, 655.0), PVector(801.0, 610.0)),
                       (PVector(801.0, 610.0), PVector(793.0, 552.0)),
                       (PVector(793.0, 552.0), PVector(767.0, 495.0)),
                       (PVector(767.0, 495.0), PVector(754.0, 429.0)),
                       (PVector(754.0, 429.0), PVector(764.0, 364.0)),
                       (PVector(764.0, 364.0), PVector(800.0, 318.0)),
                       (PVector(800.0, 318.0), PVector(846.0, 283.0)),
                       (PVector(846.0, 283.0), PVector(873.0, 236.0)),
                       (PVector(873.0, 236.0), PVector(869.0, 198.0)),
                       (PVector(869.0, 198.0), PVector(838.0, 174.0)),
                       (PVector(838.0, 174.0), PVector(762.0, 159.0)),
                       (PVector(762.0, 159.0), PVector(689.0, 176.0)),
                       (PVector(689.0, 176.0), PVector(630.0, 178.0)),
                       (PVector(630.0, 178.0), PVector(580.0, 174.0)),
                       (PVector(580.0, 174.0), PVector(527.0, 185.0)),
                       (PVector(527.0, 185.0), PVector(454.0, 196.0)),
                       (PVector(454.0, 196.0), PVector(351.0, 200.0)),
                       (PVector(351.0, 200.0), PVector(219.0, 212.0)),
                       (PVector(219.0, 212.0), PVector(193.0, 242.0)),
                       (PVector(193.0, 242.0), PVector(188.0, 294.0)),
                       (PVector(188.0, 294.0), PVector(196.0, 314.0)),
                       (PVector(196.0, 314.0), PVector(191.0, 368.0)),
                       (PVector(191.0, 368.0), PVector(202.0, 409.0)),
                       (PVector(202.0, 409.0), PVector(228.0, 417.0)),
                       (PVector(228.0, 417.0), PVector(267.0, 456.0)),
                       (PVector(267.0, 456.0), PVector(268.0, 507.0)),
                       (PVector(268.0, 507.0), PVector(271.0, 554.0)),
                       (PVector(271.0, 554.0), PVector(292.0, 583.0)),
                       (PVector(292.0, 583.0), PVector(328.0, 620.0)),
                       (PVector(328.0, 620.0), PVector(358.0, 650.0)),
                       (PVector(358.0, 650.0), PVector(391.0, 672.0)),
                       (PVector(391.0, 672.0), PVector(433.0, 695.0)),
                       ## Island Right
                       (PVector(754.0, 779.0), PVector(784.0, 793.0)),
                       (PVector(784.0, 793.0), PVector(814.0, 784.0)),
                       (PVector(814.0, 784.0), PVector(855.0, 761.0)),
                       (PVector(855.0, 761.0), PVector(885.0, 709.0)),
                       (PVector(885.0, 709.0), PVector(871.0, 667.0)),
                       (PVector(871.0, 667.0), PVector(839.0, 664.0)),
                       (PVector(839.0, 664.0), PVector(821.0, 681.0)),
                       (PVector(821.0, 681.0), PVector(802.0, 701.0)),
                       (PVector(802.0, 701.0), PVector(777.0, 732.0)),
                       (PVector(777.0, 732.0), PVector(754.0, 779.0)),
                       ## Island Left
                       (PVector(148.0, 479.0), PVector(121.0, 509.0)),
                       (PVector(121.0, 509.0), PVector(133.0, 550.0)),
                       (PVector(133.0, 550.0), PVector(179.0, 554.0)),
                       (PVector(179.0, 554.0), PVector(212.0, 512.0)),
                       (PVector(212.0, 512.0), PVector(191.0, 483.0)),
                       (PVector(191.0, 483.0), PVector(148.0, 479.0))]
        
        self.checkpoints2 = [(PVector(466.0, 709.0), PVector(449.0, 777.0), 0),
                               (PVector(527.0, 727.0), PVector(519.0, 786.0), 1),
                               (PVector(588.0, 733.0), PVector(587.0, 791.0), 2),
                               (PVector(648.0, 735.0), PVector(651.0, 800.0), 3),
                               (PVector(701.0, 724.0), PVector(732.0, 831.0), 4),
                               (PVector(749.0, 690.0), PVector(829.0, 829.0), 5),
                               (PVector(788.0, 654.0), PVector(915.0, 761.0), 6),
                               (PVector(802.0, 607.0), PVector(929.0, 636.0), 7),
                               (PVector(795.0, 557.0), PVector(869.0, 558.0), 8),
                               (PVector(775.0, 511.0), PVector(841.0, 509.0), 9),
                               (PVector(761.0, 457.0), PVector(825.0, 466.0), 10),
                               (PVector(759.0, 400.0), PVector(836.0, 416.0), 11),
                               (PVector(777.0, 346.0), PVector(857.0, 370.0), 12),
                               (PVector(834.0, 294.0), PVector(898.0, 335.0), 13),
                               (PVector(866.0, 248.0), PVector(939.0, 280.0), 14),
                               (PVector(870.0, 208.0), PVector(949.0, 199.0), 15),
                               (PVector(841.0, 176.0), PVector(875.0, 114.0), 16),
                               (PVector(775.0, 162.0), PVector(790.0, 91.0), 17),
                               (PVector(719.0, 169.0), PVector(712.0, 87.0), 18),
                               (PVector(655.0, 176.0), PVector(648.0, 97.0), 19),
                               (PVector(581.0, 174.0), PVector(577.0, 90.0), 20),
                               (PVector(505.0, 189.0), PVector(499.0, 91.0), 21),
                               (PVector(437.0, 196.0), PVector(424.0, 115.0), 22),
                               (PVector(385.0, 195.0), PVector(367.0, 133.0), 23),
                               (PVector(327.0, 202.0), PVector(313.0, 141.0), 24),
                               (PVector(263.0, 206.0), PVector(253.0, 140.0), 25),
                               (PVector(216.0, 212.0), PVector(187.0, 144.0), 26),
                               (PVector(194.0, 241.0), PVector(106.0, 200.0), 27),
                               (PVector(190.0, 283.0), PVector(102.0, 283.0), 28),
                               (PVector(194.0, 339.0), PVector(123.0, 351.0), 29),
                               (PVector(200.0, 400.0), PVector(119.0, 405.0), 30),
                               (PVector(66.0, 464.0), PVector(259.0, 448.0), 31),
                               (PVector(66.0, 555.0), PVector(268.0, 505.0), 32),
                               (PVector(135.0, 621.0), PVector(274.0, 559.0), 33),
                               (PVector(259.0, 637.0), PVector(304.0, 595.0), 34),
                               (PVector(307.0, 670.0), PVector(342.0, 635.0), 35),
                               (PVector(336.0, 703.0), PVector(373.0, 658.0), 36)]
        
