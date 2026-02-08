//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index
// ID_model: CRWD_1Min_1M00_8d4bd386 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_CRWD_1Min_1M00_8d4bd386", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_CRWD_1Min_8d4bd386(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Positive_Money_Flow_Sum <= 1.36362e+06 )
		if( Positive_Money_Flow_Sum <= 469359 )
			if( Typical_Price <= 272.956 )
				if( MFI_Low <= -10.8712 )
					if( Typical_Price <= 259.595 )
						if( Negative_Money_Flow <= 6.38145e+06 )
							if( Positive_Money_Flow_Sum <= 83351.9 )
								ret := 0.166667
							if( Positive_Money_Flow_Sum > 83351.9 )
								if( Negative_Money_Flow <= 133889 )
									ret := 0.000000
								if( Negative_Money_Flow > 133889 )
									ret := -0.142857
						if( Negative_Money_Flow > 6.38145e+06 )
							ret := 0.600000
					if( Typical_Price > 259.595 )
						if( Money_Flow_Ratio <= 0.003501 )
							ret := 0.000000
						if( Money_Flow_Ratio > 0.003501 )
							if( Negative_Money_Flow <= 44701.9 )
								ret := 0.285714
							if( Negative_Money_Flow > 44701.9 )
								if( Money_Flow_Ratio <= 0.082451 )
									ret := 1.000000 // buy
								if( Money_Flow_Ratio > 0.082451 )
									ret := 0.750000 // buy
				if( MFI_Low > -10.8712 )
					if( Positive_Money_Flow_Sum <= 320792 )
						if( Raw_Money_Flow <= 202611 )
							if( Positive_Money_Flow_Sum <= 189006 )
								if( Positive_Money_Flow_Sum <= 183163 )
									ret := -0.416667
								if( Positive_Money_Flow_Sum > 183163 )
									ret := 0.500000
							if( Positive_Money_Flow_Sum > 189006 )
								if( Negative_Money_Flow <= 59086.1 )
									ret := -0.581395
								if( Negative_Money_Flow > 59086.1 )
									ret := -0.951220 // sell
						if( Raw_Money_Flow > 202611 )
							if( Raw_Money_Flow <= 462853 )
								if( Negative_Money_Flow <= 123702 )
									ret := 1.000000 // buy
								if( Negative_Money_Flow > 123702 )
									ret := -0.117647
							if( Raw_Money_Flow > 462853 )
								if( Raw_Money_Flow <= 530268 )
									ret := -1.000000 // sell
								if( Raw_Money_Flow > 530268 )
									ret := -0.750000 // sell
					if( Positive_Money_Flow_Sum > 320792 )
						if( Raw_Money_Flow <= 68853.8 )
							if( MFI <= 28.4395 )
								if( MFI_High <= -66.0632 )
									ret := -0.100000
								if( MFI_High > -66.0632 )
									ret := 0.729730 // buy
							if( MFI > 28.4395 )
								if( Typical_Price <= 240.134 )
									ret := -0.733333 // sell
								if( Typical_Price > 240.134 )
									ret := 0.000000
						if( Raw_Money_Flow > 68853.8 )
							if( Raw_Money_Flow <= 631873 )
								if( MFI_Low <= -7.8077 )
									ret := -1.000000 // sell
								if( MFI_Low > -7.8077 )
									ret := -0.281481
							if( Raw_Money_Flow > 631873 )
								if( Money_Flow_Ratio <= 0.146978 )
									ret := 0.833333 // buy
								if( Money_Flow_Ratio > 0.146978 )
									ret := 0.400000
			if( Typical_Price > 272.956 )
				if( MFI_High <= -43.3463 )
					if( Money_Flow_Ratio <= 0.405086 )
						if( Money_Flow_Ratio <= 0.277625 )
							if( Negative_Money_Flow_Sum <= 909072 )
								if( MFI <= 19.4104 )
									ret := -0.750000 // sell
								if( MFI > 19.4104 )
									ret := -1.000000 // sell
							if( Negative_Money_Flow_Sum > 909072 )
								if( MFI_Low <= -16.77 )
									ret := -0.152542
								if( MFI_Low > -16.77 )
									ret := 0.316547
						if( Money_Flow_Ratio > 0.277625 )
							if( Positive_Money_Flow_Sum <= 423681 )
								if( MFI_High <= -56.9055 )
									ret := -0.400000
								if( MFI_High > -56.9055 )
									ret := 0.230769
							if( Positive_Money_Flow_Sum > 423681 )
								if( Positive_Money_Flow <= 53678.3 )
									ret := -0.850000 // sell
								if( Positive_Money_Flow > 53678.3 )
									ret := 0.000000
					if( Money_Flow_Ratio > 0.405086 )
						if( Typical_Price <= 274.183 )
							ret := 0.000000
						if( Typical_Price > 274.183 )
							if( Raw_Money_Flow <= 72784 )
								if( Positive_Money_Flow <= 42410.8 )
									ret := 0.918919 // buy
								if( Positive_Money_Flow > 42410.8 )
									ret := 0.428571
							if( Raw_Money_Flow > 72784 )
								if( Money_Flow_Ratio <= 0.413236 )
									ret := 1.000000 // buy
								if( Money_Flow_Ratio > 0.413236 )
									ret := 0.428571
				if( MFI_High > -43.3463 )
					if( Negative_Money_Flow_Sum <= 418917 )
						if( Negative_Money_Flow_Sum <= 398669 )
							ret := -0.500000
						if( Negative_Money_Flow_Sum > 398669 )
							ret := -1.000000 // sell
					if( Negative_Money_Flow_Sum > 418917 )
						if( MFI_High <= -42.7542 )
							if( Negative_Money_Flow <= 28890.9 )
								ret := -1.000000 // sell
							if( Negative_Money_Flow > 28890.9 )
								ret := -0.250000
						if( MFI_High > -42.7542 )
							if( MFI_High <= -34.851 )
								if( Negative_Money_Flow_Sum <= 610533 )
									ret := 0.000000
								if( Negative_Money_Flow_Sum > 610533 )
									ret := 0.875000 // buy
							if( MFI_High > -34.851 )
								if( MFI_Low <= 26.2451 )
									ret := -0.750000 // sell
								if( MFI_Low > 26.2451 )
									ret := -0.200000
		if( Positive_Money_Flow_Sum > 469359 )
			if( Raw_Money_Flow <= 1.01908e+06 )
				if( Negative_Money_Flow_Sum <= 8.1606e+06 )
					if( Typical_Price <= 323.671 )
						if( Negative_Money_Flow <= 31526.2 )
							if( Positive_Money_Flow <= 373198 )
								if( Negative_Money_Flow_Sum <= 1.02711e+06 )
									ret := 0.060105
								if( Negative_Money_Flow_Sum > 1.02711e+06 )
									ret := 0.193520
							if( Positive_Money_Flow > 373198 )
								if( Positive_Money_Flow <= 786824 )
									ret := 0.555556
								if( Positive_Money_Flow > 786824 )
									ret := -0.750000 // sell
						if( Negative_Money_Flow > 31526.2 )
							if( Money_Flow_Ratio <= 0.13439 )
								if( Typical_Price <= 277.996 )
									ret := 0.513514
								if( Typical_Price > 277.996 )
									ret := 0.966667 // buy
							if( Money_Flow_Ratio > 0.13439 )
								if( Negative_Money_Flow_Sum <= 822957 )
									ret := 0.401835
								if( Negative_Money_Flow_Sum > 822957 )
									ret := 0.190311
					if( Typical_Price > 323.671 )
						if( Negative_Money_Flow_Sum <= 1.9688e+06 )
							if( Positive_Money_Flow_Sum <= 600038 )
								if( Negative_Money_Flow_Sum <= 1.26073e+06 )
									ret := 0.738095 // buy
								if( Negative_Money_Flow_Sum > 1.26073e+06 )
									ret := 0.156250
							if( Positive_Money_Flow_Sum > 600038 )
								if( Negative_Money_Flow_Sum <= 1.38948e+06 )
									ret := -0.060071
								if( Negative_Money_Flow_Sum > 1.38948e+06 )
									ret := 0.212435
						if( Negative_Money_Flow_Sum > 1.9688e+06 )
							if( Positive_Money_Flow <= 553818 )
								if( Positive_Money_Flow_Sum <= 1.31028e+06 )
									ret := -0.287719
								if( Positive_Money_Flow_Sum > 1.31028e+06 )
									ret := 0.526316
							if( Positive_Money_Flow > 553818 )
								ret := 1.000000 // buy
				if( Negative_Money_Flow_Sum > 8.1606e+06 )
					if( MFI_Low <= -12.1087 )
						if( Negative_Money_Flow_Sum <= 1.3587e+07 )
							if( Positive_Money_Flow_Sum <= 828543 )
								if( Money_Flow_Ratio <= 0.05661 )
									ret := -1.000000 // sell
								if( Money_Flow_Ratio > 0.05661 )
									ret := 0.333333
							if( Positive_Money_Flow_Sum > 828543 )
								if( Money_Flow_Ratio <= 0.071223 )
									ret := -0.750000 // sell
								if( Money_Flow_Ratio > 0.071223 )
									ret := -1.000000 // sell
						if( Negative_Money_Flow_Sum > 1.3587e+07 )
							if( Positive_Money_Flow_Sum <= 742986 )
								if( Negative_Money_Flow_Sum <= 1.4269e+07 )
									ret := 0.875000 // buy
								if( Negative_Money_Flow_Sum > 1.4269e+07 )
									ret := -0.461538
							if( Positive_Money_Flow_Sum > 742986 )
								if( Typical_Price <= 315.46 )
									ret := 0.151515
								if( Typical_Price > 315.46 )
									ret := 0.694444
					if( MFI_Low > -12.1087 )
						if( MFI_Low <= -8.51924 )
							if( Negative_Money_Flow_Sum <= 1.44322e+07 )
								if( Negative_Money_Flow_Sum <= 1.09433e+07 )
									ret := -0.727273 // sell
								if( Negative_Money_Flow_Sum > 1.09433e+07 )
									ret := -0.958333 // sell
							if( Negative_Money_Flow_Sum > 1.44322e+07 )
								ret := 0.000000
						if( MFI_Low > -8.51924 )
							ret := 0.000000
			if( Raw_Money_Flow > 1.01908e+06 )
				if( Negative_Money_Flow_Sum <= 1.10796e+07 )
					if( MFI_High <= -53.2885 )
						if( MFI_Low <= -8.41918 )
							if( MFI <= 7.67885 )
								ret := 1.000000 // buy
							if( MFI > 7.67885 )
								if( Money_Flow_Ratio <= 0.098592 )
									ret := 0.600000
								if( Money_Flow_Ratio > 0.098592 )
									ret := 0.000000
						if( MFI_Low > -8.41918 )
							if( Negative_Money_Flow <= 1.19139e+06 )
								if( MFI_Low <= 1.8763 )
									ret := 0.666667
								if( MFI_Low > 1.8763 )
									ret := 0.250000
							if( Negative_Money_Flow > 1.19139e+06 )
								if( MFI_Low <= 0.233833 )
									ret := 1.000000 // buy
								if( MFI_Low > 0.233833 )
									ret := 0.913043 // buy
					if( MFI_High > -53.2885 )
						if( Negative_Money_Flow_Sum <= 2.63607e+06 )
							if( Typical_Price <= 320.11 )
								if( Raw_Money_Flow <= 1.44492e+06 )
									ret := 1.000000 // buy
								if( Raw_Money_Flow > 1.44492e+06 )
									ret := 0.500000
							if( Typical_Price > 320.11 )
								ret := -0.250000
						if( Negative_Money_Flow_Sum > 2.63607e+06 )
							ret := -0.750000 // sell
				if( Negative_Money_Flow_Sum > 1.10796e+07 )
					if( Negative_Money_Flow_Sum <= 8.32862e+07 )
						if( Negative_Money_Flow_Sum <= 3.14227e+07 )
							if( MFI_Low <= -15.893 )
								if( Negative_Money_Flow_Sum <= 2.30216e+07 )
									ret := 0.777778 // buy
								if( Negative_Money_Flow_Sum > 2.30216e+07 )
									ret := 0.333333
							if( MFI_Low > -15.893 )
								if( Negative_Money_Flow_Sum <= 2.23293e+07 )
									ret := -0.307692
								if( Negative_Money_Flow_Sum > 2.23293e+07 )
									ret := 0.533333
						if( Negative_Money_Flow_Sum > 3.14227e+07 )
							if( Negative_Money_Flow_Sum <= 3.64362e+07 )
								if( Positive_Money_Flow_Sum <= 669982 )
									ret := -1.000000 // sell
								if( Positive_Money_Flow_Sum > 669982 )
									ret := -0.800000 // sell
							if( Negative_Money_Flow_Sum > 3.64362e+07 )
								if( Raw_Money_Flow <= 6.39638e+06 )
									ret := 0.600000
								if( Raw_Money_Flow > 6.39638e+06 )
									ret := -0.454545
					if( Negative_Money_Flow_Sum > 8.32862e+07 )
						ret := 1.000000 // buy
	if( Positive_Money_Flow_Sum > 1.36362e+06 )
		if( Negative_Money_Flow_Sum <= 4.64219e+07 )
			if( Positive_Money_Flow <= 55.3324 )
				if( Raw_Money_Flow <= 140924 )
					if( Typical_Price <= 232.226 )
						if( MFI_Low <= 16.8636 )
							if( MFI_Low <= 4.23454 )
								ret := 1.000000 // buy
							if( MFI_Low > 4.23454 )
								ret := 0.333333
						if( MFI_Low > 16.8636 )
							if( Negative_Money_Flow <= 125216 )
								if( Typical_Price <= 227.45 )
									ret := -0.026316
								if( Typical_Price > 227.45 )
									ret := -0.535714
							if( Negative_Money_Flow > 125216 )
								if( MFI <= 58.5098 )
									ret := -0.250000
								if( MFI > 58.5098 )
									ret := 0.500000
					if( Typical_Price > 232.226 )
						if( Negative_Money_Flow_Sum <= 889496 )
							if( MFI_Low <= 43.7166 )
								if( Positive_Money_Flow_Sum <= 1.41149e+06 )
									ret := -0.250000
								if( Positive_Money_Flow_Sum > 1.41149e+06 )
									ret := -0.888889 // sell
							if( MFI_Low > 43.7166 )
								if( Positive_Money_Flow_Sum <= 2.9631e+06 )
									ret := 0.180488
								if( Positive_Money_Flow_Sum > 2.9631e+06 )
									ret := -0.164179
						if( Negative_Money_Flow_Sum > 889496 )
							if( Typical_Price <= 254.276 )
								if( Positive_Money_Flow_Sum <= 3.93669e+06 )
									ret := 0.680412
								if( Positive_Money_Flow_Sum > 3.93669e+06 )
									ret := 0.078947
							if( Typical_Price > 254.276 )
								if( MFI <= 64.2319 )
									ret := 0.152239
								if( MFI > 64.2319 )
									ret := 0.327586
				if( Raw_Money_Flow > 140924 )
					if( Typical_Price <= 200.062 )
						if( Positive_Money_Flow_Sum <= 4.67066e+06 )
							ret := 1.000000 // buy
						if( Positive_Money_Flow_Sum > 4.67066e+06 )
							if( Money_Flow_Ratio <= 2.24827 )
								ret := -0.250000
							if( Money_Flow_Ratio > 2.24827 )
								ret := 0.500000
					if( Typical_Price > 200.062 )
						if( Positive_Money_Flow_Sum <= 1.36569e+06 )
							ret := -1.000000 // sell
						if( Positive_Money_Flow_Sum > 1.36569e+06 )
							if( Negative_Money_Flow_Sum <= 8.59884e+06 )
								if( Negative_Money_Flow_Sum <= 4.4212e+06 )
									ret := 0.075198
								if( Negative_Money_Flow_Sum > 4.4212e+06 )
									ret := -0.038188
							if( Negative_Money_Flow_Sum > 8.59884e+06 )
								if( Money_Flow_Ratio <= 2.47209 )
									ret := 0.051364
								if( Money_Flow_Ratio > 2.47209 )
									ret := 0.191352
			if( Positive_Money_Flow > 55.3324 )
				if( Raw_Money_Flow <= 178153 )
					if( Negative_Money_Flow_Sum <= 2.35429e+07 )
						if( Positive_Money_Flow_Sum <= 1.50512e+06 )
							if( MFI_High <= -32.033 )
								if( Negative_Money_Flow_Sum <= 2.16312e+06 )
									ret := -0.766667 // sell
								if( Negative_Money_Flow_Sum > 2.16312e+06 )
									ret := -0.147059
							if( MFI_High > -32.033 )
								if( MFI_Low <= 37.4781 )
									ret := 0.744186 // buy
								if( MFI_Low > 37.4781 )
									ret := 0.156522
						if( Positive_Money_Flow_Sum > 1.50512e+06 )
							if( Positive_Money_Flow_Sum <= 1.90434e+06 )
								if( Money_Flow_Ratio <= 1.2813 )
									ret := -0.141304
								if( Money_Flow_Ratio > 1.2813 )
									ret := -0.439114
							if( Positive_Money_Flow_Sum > 1.90434e+06 )
								if( Positive_Money_Flow_Sum <= 2.09094e+06 )
									ret := 0.259615
								if( Positive_Money_Flow_Sum > 2.09094e+06 )
									ret := -0.109677
					if( Negative_Money_Flow_Sum > 2.35429e+07 )
						if( Money_Flow_Ratio <= 2.40081 )
							if( Typical_Price <= 306.807 )
								if( Raw_Money_Flow <= 40026.8 )
									ret := -0.500000
								if( Raw_Money_Flow > 40026.8 )
									ret := 0.111111
							if( Typical_Price > 306.807 )
								if( Negative_Money_Flow_Sum <= 2.41752e+07 )
									ret := -1.000000 // sell
								if( Negative_Money_Flow_Sum > 2.41752e+07 )
									ret := -0.500000
						if( Money_Flow_Ratio > 2.40081 )
							if( Money_Flow_Ratio <= 3.10935 )
								ret := -1.000000 // sell
							if( Money_Flow_Ratio > 3.10935 )
								if( Raw_Money_Flow <= 78706.1 )
									ret := -0.689655
								if( Raw_Money_Flow > 78706.1 )
									ret := -0.350000
				if( Raw_Money_Flow > 178153 )
					if( Typical_Price <= 231.99 )
						if( Negative_Money_Flow_Sum <= 2.9643e+06 )
							if( Positive_Money_Flow <= 229357 )
								if( MFI_High <= -14.7609 )
									ret := 0.117647
								if( MFI_High > -14.7609 )
									ret := 0.782609 // buy
							if( Positive_Money_Flow > 229357 )
								if( Raw_Money_Flow <= 274233 )
									ret := -0.722222 // sell
								if( Raw_Money_Flow > 274233 )
									ret := -0.161290
						if( Negative_Money_Flow_Sum > 2.9643e+06 )
							if( Raw_Money_Flow <= 1.27047e+06 )
								if( MFI_High <= -48.9838 )
									ret := 0.269231
								if( MFI_High > -48.9838 )
									ret := 0.719298 // buy
							if( Raw_Money_Flow > 1.27047e+06 )
								if( Typical_Price <= 215.533 )
									ret := 0.703125 // buy
								if( Typical_Price > 215.533 )
									ret := 0.126174
					if( Typical_Price > 231.99 )
						if( Negative_Money_Flow_Sum <= 3.62835e+07 )
							if( Money_Flow_Ratio <= 200.334 )
								if( Positive_Money_Flow_Sum <= 8.73194e+07 )
									ret := 0.023695
								if( Positive_Money_Flow_Sum > 8.73194e+07 )
									ret := -0.172745
							if( Money_Flow_Ratio > 200.334 )
								ret := 1.000000 // buy
						if( Negative_Money_Flow_Sum > 3.62835e+07 )
							if( MFI_Low <= 36.9811 )
								if( Positive_Money_Flow <= 3.50281e+06 )
									ret := -0.069663
								if( Positive_Money_Flow > 3.50281e+06 )
									ret := -0.276527
							if( MFI_Low > 36.9811 )
								if( Positive_Money_Flow_Sum <= 2.16174e+08 )
									ret := -0.018476
								if( Positive_Money_Flow_Sum > 2.16174e+08 )
									ret := 0.446809
		if( Negative_Money_Flow_Sum > 4.64219e+07 )
			if( Negative_Money_Flow_Sum <= 1.03736e+08 )
				if( Typical_Price <= 380.563 )
					if( Positive_Money_Flow_Sum <= 1.73841e+08 )
						if( MFI_Low <= 51.697 )
							if( Raw_Money_Flow <= 6.74073e+06 )
								if( Negative_Money_Flow_Sum <= 6.14255e+07 )
									ret := 0.175684
								if( Negative_Money_Flow_Sum > 6.14255e+07 )
									ret := -0.001699
							if( Raw_Money_Flow > 6.74073e+06 )
								if( Positive_Money_Flow_Sum <= 1.39166e+08 )
									ret := 0.230055
								if( Positive_Money_Flow_Sum > 1.39166e+08 )
									ret := -0.085526
						if( MFI_Low > 51.697 )
							if( Money_Flow_Ratio <= 3.15175 )
								if( Negative_Money_Flow <= 1.08097e+07 )
									ret := -0.576923
								if( Negative_Money_Flow > 1.08097e+07 )
									ret := 0.250000
							if( Money_Flow_Ratio > 3.15175 )
								if( Positive_Money_Flow_Sum <= 1.72157e+08 )
									ret := 0.529412
								if( Positive_Money_Flow_Sum > 1.72157e+08 )
									ret := -0.400000
					if( Positive_Money_Flow_Sum > 1.73841e+08 )
						if( Typical_Price <= 240.93 )
							if( Negative_Money_Flow_Sum <= 5.63945e+07 )
								ret := -0.200000
							if( Negative_Money_Flow_Sum > 5.63945e+07 )
								if( Negative_Money_Flow_Sum <= 6.95899e+07 )
									ret := -1.000000 // sell
								if( Negative_Money_Flow_Sum > 6.95899e+07 )
									ret := -0.666667
						if( Typical_Price > 240.93 )
							if( Positive_Money_Flow <= 1.03078e+08 )
								if( Positive_Money_Flow_Sum <= 3.44276e+08 )
									ret := 0.518033
								if( Positive_Money_Flow_Sum > 3.44276e+08 )
									ret := -0.176471
							if( Positive_Money_Flow > 1.03078e+08 )
								ret := -1.000000 // sell
				if( Typical_Price > 380.563 )
					if( Negative_Money_Flow_Sum <= 8.97422e+07 )
						if( Positive_Money_Flow_Sum <= 4.95051e+07 )
							if( Raw_Money_Flow <= 8.02854e+06 )
								if( Positive_Money_Flow_Sum <= 1.13939e+07 )
									ret := -0.769231 // sell
								if( Positive_Money_Flow_Sum > 1.13939e+07 )
									ret := -0.102941
							if( Raw_Money_Flow > 8.02854e+06 )
								if( Positive_Money_Flow_Sum <= 3.35174e+07 )
									ret := 0.428571
								if( Positive_Money_Flow_Sum > 3.35174e+07 )
									ret := 0.000000
						if( Positive_Money_Flow_Sum > 4.95051e+07 )
							if( Raw_Money_Flow <= 6.67492e+06 )
								if( Positive_Money_Flow_Sum <= 5.15562e+07 )
									ret := -0.428571
								if( Positive_Money_Flow_Sum > 5.15562e+07 )
									ret := 0.125000
							if( Raw_Money_Flow > 6.67492e+06 )
								if( Typical_Price <= 387.232 )
									ret := -0.469880
								if( Typical_Price > 387.232 )
									ret := -0.875000 // sell
					if( Negative_Money_Flow_Sum > 8.97422e+07 )
						if( MFI <= 47.5609 )
							if( Positive_Money_Flow <= 6.46741e+06 )
								if( Negative_Money_Flow <= 1.45228e+07 )
									ret := -0.133333
								if( Negative_Money_Flow > 1.45228e+07 )
									ret := 0.750000 // buy
							if( Positive_Money_Flow > 6.46741e+06 )
								if( MFI_High <= -42.3067 )
									ret := 0.800000 // buy
								if( MFI_High > -42.3067 )
									ret := 0.250000
						if( MFI > 47.5609 )
							if( MFI_High <= -9.70537 )
								ret := 1.000000 // buy
							if( MFI_High > -9.70537 )
								ret := 0.500000
			if( Negative_Money_Flow_Sum > 1.03736e+08 )
				if( Positive_Money_Flow_Sum <= 4.37085e+08 )
					if( Negative_Money_Flow_Sum <= 2.37088e+08 )
						if( Typical_Price <= 286.08 )
							if( MFI_High <= -28.5213 )
								if( Negative_Money_Flow_Sum <= 1.46639e+08 )
									ret := -0.136784
								if( Negative_Money_Flow_Sum > 1.46639e+08 )
									ret := 0.157360
							if( MFI_High > -28.5213 )
								if( MFI_Low <= 37.8207 )
									ret := -0.562500
								if( MFI_Low > 37.8207 )
									ret := -0.099174
						if( Typical_Price > 286.08 )
							if( Raw_Money_Flow <= 3.0506e+07 )
								if( Positive_Money_Flow_Sum <= 1.30257e+08 )
									ret := 0.112694
								if( Positive_Money_Flow_Sum > 1.30257e+08 )
									ret := 0.489270
							if( Raw_Money_Flow > 3.0506e+07 )
								if( Negative_Money_Flow <= 3.231e+07 )
									ret := -0.561404
								if( Negative_Money_Flow > 3.231e+07 )
									ret := 0.139535
					if( Negative_Money_Flow_Sum > 2.37088e+08 )
						if( MFI <= 56.6598 )
							if( MFI <= 43.6042 )
								if( Positive_Money_Flow <= 7.72607e+07 )
									ret := -0.171577
								if( Positive_Money_Flow > 7.72607e+07 )
									ret := 0.722222 // buy
							if( MFI > 43.6042 )
								if( Positive_Money_Flow <= 3.77602e+06 )
									ret := -0.607143
								if( Positive_Money_Flow > 3.77602e+06 )
									ret := -0.870968 // sell
						if( MFI > 56.6598 )
							ret := 1.000000 // buy
				if( Positive_Money_Flow_Sum > 4.37085e+08 )
					if( Money_Flow_Ratio <= 2.1046 )
						if( MFI_High <= -35.7624 )
							if( Typical_Price <= 380.227 )
								if( Positive_Money_Flow <= 6.69181e+07 )
									ret := 0.200000
								if( Positive_Money_Flow > 6.69181e+07 )
									ret := -0.250000
							if( Typical_Price > 380.227 )
								ret := -0.750000 // sell
						if( MFI_High > -35.7624 )
							if( Negative_Money_Flow <= 5.06025e+07 )
								if( Negative_Money_Flow <= 483462 )
									ret := 0.805556 // buy
								if( Negative_Money_Flow > 483462 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow > 5.06025e+07 )
								if( Positive_Money_Flow_Sum <= 6.36208e+08 )
									ret := -0.800000 // sell
								if( Positive_Money_Flow_Sum > 6.36208e+08 )
									ret := 1.000000 // buy
					if( Money_Flow_Ratio > 2.1046 )
						if( Typical_Price <= 381.553 )
							if( Typical_Price <= 269.49 )
								if( Typical_Price <= 268.103 )
									ret := 0.600000
								if( Typical_Price > 268.103 )
									ret := 1.000000 // buy
							if( Typical_Price > 269.49 )
								if( Negative_Money_Flow_Sum <= 3.19388e+08 )
									ret := -0.707692 // sell
								if( Negative_Money_Flow_Sum > 3.19388e+08 )
									ret := 0.384615
						if( Typical_Price > 381.553 )
							if( Typical_Price <= 383.69 )
								if( Negative_Money_Flow_Sum <= 2.52374e+08 )
									ret := 0.750000 // buy
								if( Negative_Money_Flow_Sum > 2.52374e+08 )
									ret := 1.000000 // buy
							if( Typical_Price > 383.69 )
								ret := -0.166667
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Money_Flow_Index 
//@version=5
//indicator title="Money Flow Index (MFI)", shorttitle="MFI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)

// Input parameters
length_MFI = input.int(14, minval=1, title="MFI Length")

// Calculate the Typical Price
Typical_Price = (high + low + close) / 3

// Calculate Raw Money Flow
Raw_Money_Flow = Typical_Price * volume

// Calculate Positive and Negative Money Flow
Positive_Money_Flow = Raw_Money_Flow * (Typical_Price > Typical_Price[1] ? 1 : 0)
Negative_Money_Flow = Raw_Money_Flow * (Typical_Price < Typical_Price[1] ? 1 : 0)

// Sum of Positive and Negative Money Flow over the given length
Positive_Money_Flow_Sum = ta.sma(Positive_Money_Flow, length_MFI) * length_MFI
Negative_Money_Flow_Sum = ta.sma(Negative_Money_Flow, length_MFI) * length_MFI

// Calculate Money Flow Ratio
Money_Flow_Ratio = Positive_Money_Flow_Sum / Negative_Money_Flow_Sum

// Calculate MFI
MFI = 100 - (100 / (1 + Money_Flow_Ratio))

// Calculate MFI high and low bands
MFI_High = MFI - 80
MFI_Low = MFI - 20

// Plot the MFI
plot(MFI, color=color.blue, title="MFI")

// Plot the MFI high and low bands
hline(80, "MFI High", color=color.red, linestyle=hline.style_dashed)
hline(20, "MFI Low", color=color.green, linestyle=hline.style_dashed)
plot(MFI_High, color=color.red, title="MFI High Band")
plot(MFI_Low, color=color.green, title="MFI Low Band")

// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_CRWD_1Min_8d4bd386(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.


