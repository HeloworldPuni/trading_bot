//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Vortex_Indicator
// ID_model: ADBE_15Min_2MV0_7989e3b3 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ADBE_15Min_2MV0_7989e3b3", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ADBE_15Min_7989e3b3(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, VIP, VIM, VIP_VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( Typical_Price <= 475.411 )
		if( Raw_Money_Flow <= 1.45797e+06 )
			if( Negative_Money_Flow_Sum <= 3.43576e+08 )
				if( Negative_Money_Flow <= 284.706 )
					if( Money_Flow_Ratio <= 6.94146 )
						if( VIP <= 1.18924 )
							if( Negative_Money_Flow_Sum <= 3.31987e+08 )
								if( VIP <= 0.73166 )
									ret := 0.666667
								if( VIP > 0.73166 )
									ret := -0.040260
							if( Negative_Money_Flow_Sum > 3.31987e+08 )
								if( Negative_Money_Flow_Sum <= 3.36247e+08 )
									ret := -0.916667 // sell
								if( Negative_Money_Flow_Sum > 3.36247e+08 )
									ret := -0.387097
						if( VIP > 1.18924 )
							if( Negative_Money_Flow_Sum <= 832177 )
								if( Raw_Money_Flow <= 38916.9 )
									ret := -0.071429
								if( Raw_Money_Flow > 38916.9 )
									ret := 0.628571
							if( Negative_Money_Flow_Sum > 832177 )
								if( Raw_Money_Flow <= 58215.6 )
									ret := -0.075949
								if( Raw_Money_Flow > 58215.6 )
									ret := -0.244587
					if( Money_Flow_Ratio > 6.94146 )
						if( Positive_Money_Flow <= 789722 )
							if( MFI_High <= 19.0379 )
								if( MFI_Low <= 77.356 )
									ret := 0.094003
								if( MFI_Low > 77.356 )
									ret := 0.528571
							if( MFI_High > 19.0379 )
								if( MFI_Low <= 79.277 )
									ret := -0.619048
								if( MFI_Low > 79.277 )
									ret := -0.090395
						if( Positive_Money_Flow > 789722 )
							if( MFI <= 99.005 )
								if( VIP_VIM <= 0.720697 )
									ret := -0.081081
								if( VIP_VIM > 0.720697 )
									ret := -0.529412
							if( MFI > 99.005 )
								ret := -1.000000 // sell
				if( Negative_Money_Flow > 284.706 )
					if( MFI <= 13.0461 )
						if( Money_Flow_Ratio <= 0.086492 )
							if( MFI_Low <= -18.824 )
								if( Raw_Money_Flow <= 501314 )
									ret := 0.437500
								if( Raw_Money_Flow > 501314 )
									ret := 0.976190 // buy
							if( MFI_Low > -18.824 )
								if( Positive_Money_Flow_Sum <= 2.09037e+07 )
									ret := 0.190476
								if( Positive_Money_Flow_Sum > 2.09037e+07 )
									ret := -0.941176 // sell
						if( Money_Flow_Ratio > 0.086492 )
							if( VIP <= 1.01518 )
								ret := -0.200000
							if( VIP > 1.01518 )
								if( Raw_Money_Flow <= 321711 )
									ret := 0.643939
								if( Raw_Money_Flow > 321711 )
									ret := 0.913793 // buy
					if( MFI > 13.0461 )
						if( VIP <= 1.08661 )
							if( Positive_Money_Flow_Sum <= 2.69309e+06 )
								if( Raw_Money_Flow <= 688499 )
									ret := 0.230769
								if( Raw_Money_Flow > 688499 )
									ret := -0.741935 // sell
							if( Positive_Money_Flow_Sum > 2.69309e+06 )
								if( Negative_Money_Flow_Sum <= 4.62051e+07 )
									ret := 0.802469 // buy
								if( Negative_Money_Flow_Sum > 4.62051e+07 )
									ret := 0.248969
						if( VIP > 1.08661 )
							if( Money_Flow_Ratio <= 0.162959 )
								if( Money_Flow_Ratio <= 0.157018 )
									ret := -0.333333
								if( Money_Flow_Ratio > 0.157018 )
									ret := -0.840000 // sell
							if( Money_Flow_Ratio > 0.162959 )
								if( Negative_Money_Flow_Sum <= 1.14222e+06 )
									ret := 0.400911
								if( Negative_Money_Flow_Sum > 1.14222e+06 )
									ret := 0.063841
			if( Negative_Money_Flow_Sum > 3.43576e+08 )
				if( Negative_Money_Flow <= 876.283 )
					if( MFI_High <= -36.9618 )
						if( Positive_Money_Flow_Sum <= 1.02671e+06 )
							if( VIP_VIM <= -0.840382 )
								ret := -0.800000 // sell
							if( VIP_VIM > -0.840382 )
								ret := -0.375000
						if( Positive_Money_Flow_Sum > 1.02671e+06 )
							if( VIP <= 0.84475 )
								if( Positive_Money_Flow_Sum <= 4.4149e+07 )
									ret := -0.700000 // sell
								if( Positive_Money_Flow_Sum > 4.4149e+07 )
									ret := -0.144231
							if( VIP > 0.84475 )
								if( MFI <= 0.353551 )
									ret := 0.777778 // buy
								if( MFI > 0.353551 )
									ret := 0.024763
					if( MFI_High > -36.9618 )
						if( Raw_Money_Flow <= 211558 )
							if( Negative_Money_Flow_Sum <= 4.48319e+08 )
								if( Money_Flow_Ratio <= 1.3982 )
									ret := 0.867647 // buy
								if( Money_Flow_Ratio > 1.3982 )
									ret := 0.000000
							if( Negative_Money_Flow_Sum > 4.48319e+08 )
								if( VIM <= 1.46235 )
									ret := 0.093750
								if( VIM > 1.46235 )
									ret := -0.421053
						if( Raw_Money_Flow > 211558 )
							if( Positive_Money_Flow_Sum <= 3.63295e+08 )
								if( Negative_Money_Flow_Sum <= 3.6536e+08 )
									ret := 0.076923
								if( Negative_Money_Flow_Sum > 3.6536e+08 )
									ret := 0.842105 // buy
							if( Positive_Money_Flow_Sum > 3.63295e+08 )
								if( MFI_High <= -29.533 )
									ret := -0.548387
								if( MFI_High > -29.533 )
									ret := 0.122449
				if( Negative_Money_Flow > 876.283 )
					if( Positive_Money_Flow_Sum <= 8.19358e+08 )
						if( Negative_Money_Flow_Sum <= 4.23923e+08 )
							if( VIP_VIM <= -0.168174 )
								if( Negative_Money_Flow <= 77906.4 )
									ret := 0.584699
								if( Negative_Money_Flow > 77906.4 )
									ret := 0.120482
							if( VIP_VIM > -0.168174 )
								if( VIM <= 1.43623 )
									ret := 0.720257 // buy
								if( VIM > 1.43623 )
									ret := 0.272727
						if( Negative_Money_Flow_Sum > 4.23923e+08 )
							if( VIP_VIM <= 0.315306 )
								if( VIM <= 2.96607 )
									ret := 0.156282
								if( VIM > 2.96607 )
									ret := -0.430380
							if( VIP_VIM > 0.315306 )
								if( Positive_Money_Flow <= 25395 )
									ret := 0.511111
								if( Positive_Money_Flow > 25395 )
									ret := 0.896552 // buy
					if( Positive_Money_Flow_Sum > 8.19358e+08 )
						if( VIP_VIM <= -0.146914 )
							ret := 0.714286 // buy
						if( VIP_VIM > -0.146914 )
							if( Positive_Money_Flow <= 9517.64 )
								ret := -0.578947
							if( Positive_Money_Flow > 9517.64 )
								ret := -1.000000 // sell
		if( Raw_Money_Flow > 1.45797e+06 )
			if( Positive_Money_Flow_Sum <= 2.98149e+07 )
				if( Raw_Money_Flow <= 5.49723e+07 )
					if( Negative_Money_Flow_Sum <= 1.31559e+06 )
						if( Positive_Money_Flow <= 2.15191e+06 )
							ret := -0.500000
						if( Positive_Money_Flow > 2.15191e+06 )
							ret := -1.000000 // sell
					if( Negative_Money_Flow_Sum > 1.31559e+06 )
						if( Positive_Money_Flow_Sum <= 280058 )
							if( Typical_Price <= 396.409 )
								if( Typical_Price <= 242.72 )
									ret := 0.250000
								if( Typical_Price > 242.72 )
									ret := -0.411765
							if( Typical_Price > 396.409 )
								if( Positive_Money_Flow_Sum <= 227617 )
									ret := 0.818182 // buy
								if( Positive_Money_Flow_Sum > 227617 )
									ret := 1.000000 // buy
						if( Positive_Money_Flow_Sum > 280058 )
							if( Negative_Money_Flow <= 5.35504e+07 )
								if( VIP <= 1.46154 )
									ret := -0.180371
								if( VIP > 1.46154 )
									ret := 0.055655
							if( Negative_Money_Flow > 5.35504e+07 )
								if( Positive_Money_Flow_Sum <= 1.45422e+06 )
									ret := -1.000000 // sell
								if( Positive_Money_Flow_Sum > 1.45422e+06 )
									ret := -0.703704 // sell
				if( Raw_Money_Flow > 5.49723e+07 )
					if( Money_Flow_Ratio <= 0.034006 )
						if( MFI_Low <= -18.2774 )
							if( Negative_Money_Flow_Sum <= 1.01469e+08 )
								if( VIM <= 1.93717 )
									ret := 0.666667
								if( VIM > 1.93717 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow_Sum > 1.01469e+08 )
								if( Negative_Money_Flow <= 5.63865e+08 )
									ret := 0.074844
								if( Negative_Money_Flow > 5.63865e+08 )
									ret := -0.875000 // sell
						if( MFI_Low > -18.2774 )
							if( MFI <= 1.84542 )
								if( Positive_Money_Flow_Sum <= 2.62922e+06 )
									ret := -0.500000
								if( Positive_Money_Flow_Sum > 2.62922e+06 )
									ret := -0.833333 // sell
							if( MFI > 1.84542 )
								if( VIP_VIM <= -0.732704 )
									ret := -0.600000
								if( VIP_VIM > -0.732704 )
									ret := -0.044586
					if( Money_Flow_Ratio > 0.034006 )
						if( Positive_Money_Flow_Sum <= 2.47519e+07 )
							if( MFI_High <= -70.6356 )
								if( Positive_Money_Flow_Sum <= 5.79781e+06 )
									ret := 0.275862
								if( Positive_Money_Flow_Sum > 5.79781e+06 )
									ret := 0.821429 // buy
							if( MFI_High > -70.6356 )
								ret := -0.500000
						if( Positive_Money_Flow_Sum > 2.47519e+07 )
							ret := -0.500000
			if( Positive_Money_Flow_Sum > 2.98149e+07 )
				if( MFI_High <= -68.5792 )
					if( Negative_Money_Flow_Sum <= 5.13447e+08 )
						if( Money_Flow_Ratio <= 0.082055 )
							if( Negative_Money_Flow <= 1.25087e+06 )
								ret := -1.000000 // sell
							if( Negative_Money_Flow > 1.25087e+06 )
								if( Typical_Price <= 358.222 )
									ret := -0.666667
								if( Typical_Price > 358.222 )
									ret := -1.000000 // sell
						if( Money_Flow_Ratio > 0.082055 )
							if( MFI_Low <= -12.1663 )
								ret := 0.400000
							if( MFI_Low > -12.1663 )
								if( Negative_Money_Flow_Sum <= 4.54866e+08 )
									ret := -0.250000
								if( Negative_Money_Flow_Sum > 4.54866e+08 )
									ret := -0.724638 // sell
					if( Negative_Money_Flow_Sum > 5.13447e+08 )
						if( Raw_Money_Flow <= 3.49739e+07 )
							if( VIP_VIM <= -0.740093 )
								ret := 0.857143 // buy
							if( VIP_VIM > -0.740093 )
								if( Positive_Money_Flow_Sum <= 4.32283e+07 )
									ret := -0.961538 // sell
								if( Positive_Money_Flow_Sum > 4.32283e+07 )
									ret := -0.623188
						if( Raw_Money_Flow > 3.49739e+07 )
							if( VIP <= 0.78382 )
								if( MFI <= 8.1548 )
									ret := 0.571429
								if( MFI > 8.1548 )
									ret := 0.017857
							if( VIP > 0.78382 )
								if( Negative_Money_Flow_Sum <= 6.57913e+08 )
									ret := 0.030303
								if( Negative_Money_Flow_Sum > 6.57913e+08 )
									ret := -0.545455
				if( MFI_High > -68.5792 )
					if( Negative_Money_Flow_Sum <= 1.30063e+09 )
						if( Positive_Money_Flow_Sum <= 1.22937e+09 )
							if( Positive_Money_Flow_Sum <= 1.09033e+09 )
								if( VIP <= 1.45507 )
									ret := 0.020661
								if( VIP > 1.45507 )
									ret := -0.062870
							if( Positive_Money_Flow_Sum > 1.09033e+09 )
								if( Money_Flow_Ratio <= 4.66467 )
									ret := -0.254545
								if( Money_Flow_Ratio > 4.66467 )
									ret := -0.744681 // sell
						if( Positive_Money_Flow_Sum > 1.22937e+09 )
							if( Raw_Money_Flow <= 5.22298e+06 )
								ret := -0.125000
							if( Raw_Money_Flow > 5.22298e+06 )
								if( MFI_Low <= 64.5749 )
									ret := 0.927536 // buy
								if( MFI_Low > 64.5749 )
									ret := 0.000000
					if( Negative_Money_Flow_Sum > 1.30063e+09 )
						if( Positive_Money_Flow <= 4.63636e+06 )
							if( Positive_Money_Flow_Sum <= 8.2366e+08 )
								if( VIP_VIM <= -0.6464 )
									ret := 0.846154 // buy
								if( VIP_VIM > -0.6464 )
									ret := 0.266667
							if( Positive_Money_Flow_Sum > 8.2366e+08 )
								ret := -0.411765
						if( Positive_Money_Flow > 4.63636e+06 )
							if( MFI <= 21.8483 )
								ret := -0.666667
							if( MFI > 21.8483 )
								if( MFI <= 35.3648 )
									ret := -1.000000 // sell
								if( MFI > 35.3648 )
									ret := -0.818182 // sell
	if( Typical_Price > 475.411 )
		if( Positive_Money_Flow_Sum <= 3.18299e+07 )
			if( Positive_Money_Flow <= 2.10316e+06 )
				if( Typical_Price <= 624.984 )
					if( Money_Flow_Ratio <= 0.389538 )
						if( MFI_Low <= -15.5018 )
							if( VIP_VIM <= -0.887555 )
								if( VIP <= 0.617389 )
									ret := 0.408451
								if( VIP > 0.617389 )
									ret := -0.072727
							if( VIP_VIM > -0.887555 )
								if( Typical_Price <= 583.606 )
									ret := -0.307771
								if( Typical_Price > 583.606 )
									ret := -0.007407
						if( MFI_Low > -15.5018 )
							if( VIP_VIM <= -0.026553 )
								if( Positive_Money_Flow_Sum <= 941845 )
									ret := 0.795918 // buy
								if( Positive_Money_Flow_Sum > 941845 )
									ret := 0.098361
							if( VIP_VIM > -0.026553 )
								if( VIM <= 1.87728 )
									ret := -0.454545
								if( VIM > 1.87728 )
									ret := -1.000000 // sell
					if( Money_Flow_Ratio > 0.389538 )
						if( VIP_VIM <= -0.880543 )
							if( Positive_Money_Flow_Sum <= 3.06647e+06 )
								if( MFI <= 39.2613 )
									ret := 0.500000
								if( MFI > 39.2613 )
									ret := 1.000000 // buy
							if( Positive_Money_Flow_Sum > 3.06647e+06 )
								ret := -0.466667
						if( VIP_VIM > -0.880543 )
							if( Negative_Money_Flow <= 198029 )
								if( Money_Flow_Ratio <= 0.520931 )
									ret := -0.887755 // sell
								if( Money_Flow_Ratio > 0.520931 )
									ret := -0.393617
							if( Negative_Money_Flow > 198029 )
								if( MFI_High <= -21.7925 )
									ret := -0.329231
								if( MFI_High > -21.7925 )
									ret := 0.125984
				if( Typical_Price > 624.984 )
					if( VIM <= 6.29803 )
						if( Negative_Money_Flow_Sum <= 6.98211e+08 )
							if( MFI <= 0.610001 )
								ret := -1.000000 // sell
							if( MFI > 0.610001 )
								if( MFI <= 1.32275 )
									ret := -0.423077
								if( MFI > 1.32275 )
									ret := -0.846154 // sell
						if( Negative_Money_Flow_Sum > 6.98211e+08 )
							if( MFI_High <= -79.6938 )
								ret := -0.250000
							if( MFI_High > -79.6938 )
								ret := 0.750000 // buy
					if( VIM > 6.29803 )
						ret := 0.416667
			if( Positive_Money_Flow > 2.10316e+06 )
				if( MFI <= 72.0431 )
					if( MFI <= 51.1151 )
						if( Positive_Money_Flow_Sum <= 6.22613e+06 )
							ret := 0.761905 // buy
						if( Positive_Money_Flow_Sum > 6.22613e+06 )
							if( MFI_High <= -75.4389 )
								ret := -0.611111
							if( MFI_High > -75.4389 )
								if( VIM <= 1.31416 )
									ret := -0.400000
								if( VIM > 1.31416 )
									ret := 0.153846
					if( MFI > 51.1151 )
						if( Money_Flow_Ratio <= 1.78426 )
							ret := 0.789474 // buy
						if( Money_Flow_Ratio > 1.78426 )
							ret := 1.000000 // buy
				if( MFI > 72.0431 )
					if( VIP_VIM <= 0.380478 )
						if( Negative_Money_Flow_Sum <= 3.2066e+06 )
							ret := -0.533333
						if( Negative_Money_Flow_Sum > 3.2066e+06 )
							ret := -0.823529 // sell
					if( VIP_VIM > 0.380478 )
						ret := -0.058824
		if( Positive_Money_Flow_Sum > 3.18299e+07 )
			if( Positive_Money_Flow_Sum <= 2.9006e+08 )
				if( MFI_Low <= -11.6734 )
					if( VIP <= 1.06372 )
						if( VIP_VIM <= -0.578257 )
							if( Money_Flow_Ratio <= 0.081785 )
								if( Positive_Money_Flow <= 17298.3 )
									ret := 0.481481
								if( Positive_Money_Flow > 17298.3 )
									ret := -0.192308
							if( Money_Flow_Ratio > 0.081785 )
								ret := -0.777778 // sell
						if( VIP_VIM > -0.578257 )
							if( Positive_Money_Flow <= 160458 )
								if( MFI <= 5.76096 )
									ret := -0.452381
								if( MFI > 5.76096 )
									ret := 0.171875
							if( Positive_Money_Flow > 160458 )
								if( Typical_Price <= 547.215 )
									ret := -0.705882 // sell
								if( Typical_Price > 547.215 )
									ret := 0.083333
					if( VIP > 1.06372 )
						if( Raw_Money_Flow <= 2.01801e+06 )
							if( Positive_Money_Flow_Sum <= 3.95826e+07 )
								if( Positive_Money_Flow <= 34182.3 )
									ret := 0.500000
								if( Positive_Money_Flow > 34182.3 )
									ret := -0.304348
							if( Positive_Money_Flow_Sum > 3.95826e+07 )
								if( Raw_Money_Flow <= 154716 )
									ret := -0.944444 // sell
								if( Raw_Money_Flow > 154716 )
									ret := -0.632353
						if( Raw_Money_Flow > 2.01801e+06 )
							if( MFI <= 8.04066 )
								if( VIP_VIM <= -0.475949 )
									ret := -0.428571
								if( VIP_VIM > -0.475949 )
									ret := -0.944444 // sell
							if( MFI > 8.04066 )
								ret := -1.000000 // sell
				if( MFI_Low > -11.6734 )
					if( Money_Flow_Ratio <= 0.285244 )
						if( Positive_Money_Flow <= 3.26297e+07 )
							if( Negative_Money_Flow <= 3.21018e+08 )
								if( Negative_Money_Flow_Sum <= 1.02738e+09 )
									ret := 0.091368
								if( Negative_Money_Flow_Sum > 1.02738e+09 )
									ret := -0.248062
							if( Negative_Money_Flow > 3.21018e+08 )
								if( Raw_Money_Flow <= 4.5658e+08 )
									ret := 0.704545 // buy
								if( Raw_Money_Flow > 4.5658e+08 )
									ret := -0.333333
						if( Positive_Money_Flow > 3.26297e+07 )
							if( VIP_VIM <= 0.125926 )
								if( Raw_Money_Flow <= 6.73842e+07 )
									ret := -0.451220
								if( Raw_Money_Flow > 6.73842e+07 )
									ret := 0.337209
							if( VIP_VIM > 0.125926 )
								ret := 0.727273 // buy
					if( Money_Flow_Ratio > 0.285244 )
						if( Money_Flow_Ratio <= 107.48 )
							if( MFI <= 55.3588 )
								if( Negative_Money_Flow_Sum <= 7.41767e+08 )
									ret := -0.071929
								if( Negative_Money_Flow_Sum > 7.41767e+08 )
									ret := 0.531646
							if( MFI > 55.3588 )
								if( Negative_Money_Flow <= 2.41508e+07 )
									ret := -0.021611
								if( Negative_Money_Flow > 2.41508e+07 )
									ret := 0.173047
						if( Money_Flow_Ratio > 107.48 )
							if( VIP <= 1.75427 )
								if( VIP_VIM <= 0.635831 )
									ret := -0.823529 // sell
								if( VIP_VIM > 0.635831 )
									ret := -0.272727
							if( VIP > 1.75427 )
								if( Positive_Money_Flow_Sum <= 1.46039e+08 )
									ret := -0.684211
								if( Positive_Money_Flow_Sum > 1.46039e+08 )
									ret := 0.000000
			if( Positive_Money_Flow_Sum > 2.9006e+08 )
				if( VIM <= 0.998799 )
					if( VIM <= 0.417306 )
						ret := 1.000000 // buy
					if( VIM > 0.417306 )
						if( Money_Flow_Ratio <= 1.59922 )
							if( Typical_Price <= 598.303 )
								if( MFI_High <= -51.5502 )
									ret := -0.650000
								if( MFI_High > -51.5502 )
									ret := 0.119545
							if( Typical_Price > 598.303 )
								if( Money_Flow_Ratio <= 1.40179 )
									ret := -0.339744
								if( Money_Flow_Ratio > 1.40179 )
									ret := 0.343750
						if( Money_Flow_Ratio > 1.59922 )
							if( Positive_Money_Flow_Sum <= 1.57617e+09 )
								if( MFI_Low <= 47.3737 )
									ret := -0.210031
								if( MFI_Low > 47.3737 )
									ret := -0.001981
							if( Positive_Money_Flow_Sum > 1.57617e+09 )
								if( Typical_Price <= 560.815 )
									ret := -0.700855 // sell
								if( Typical_Price > 560.815 )
									ret := 0.000000
				if( VIM > 0.998799 )
					if( MFI <= 44.6195 )
						if( Positive_Money_Flow_Sum <= 4.46003e+08 )
							if( Negative_Money_Flow <= 2.79931e+07 )
								if( Money_Flow_Ratio <= 0.125933 )
									ret := 1.000000 // buy
								if( Money_Flow_Ratio > 0.125933 )
									ret := -0.159705
							if( Negative_Money_Flow > 2.79931e+07 )
								if( Positive_Money_Flow_Sum <= 3.33475e+08 )
									ret := 0.128713
								if( Positive_Money_Flow_Sum > 3.33475e+08 )
									ret := 0.570470
						if( Positive_Money_Flow_Sum > 4.46003e+08 )
							if( VIP_VIM <= -0.860503 )
								ret := 0.611111
							if( VIP_VIM > -0.860503 )
								if( VIP_VIM <= -0.174055 )
									ret := -0.485149
								if( VIP_VIM > -0.174055 )
									ret := -0.158537
					if( MFI > 44.6195 )
						if( MFI_High <= 2.63008 )
							if( Positive_Money_Flow_Sum <= 5.05965e+08 )
								if( Positive_Money_Flow <= 95272.7 )
									ret := 0.307692
								if( Positive_Money_Flow > 95272.7 )
									ret := 0.122412
							if( Positive_Money_Flow_Sum > 5.05965e+08 )
								if( Negative_Money_Flow_Sum <= 1.4626e+08 )
									ret := 0.647619
								if( Negative_Money_Flow_Sum > 1.4626e+08 )
									ret := -0.007319
						if( MFI_High > 2.63008 )
							if( VIP <= 2.49005 )
								if( VIP <= 1.97488 )
									ret := 0.049217
								if( VIP > 1.97488 )
									ret := -0.262357
							if( VIP > 2.49005 )
								if( MFI_Low <= 79.7526 )
									ret := 0.152381
								if( MFI_Low > 79.7526 )
									ret := 0.795918 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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


//CODE associated with the technical indicator L_Vortex_Indicator 
//@version=5
//indicator title = "Vortex Indicator", shorttitle="VI", format=format.price, precision=4, timeframe="", timeframe_gaps=true)
period_ = input.int(14, title="Length", minval=2)
VMP = math.sum( math.abs( high - low[1]), period_ )
VMM = math.sum( math.abs( low - high[1]), period_ )
STR = math.sum( ta.atr(1), period_ )
VIP = VMP / STR
VIM = VMM / STR

VIP_VIM = VIP - VIM

plot(VIP, title="VI +", color=#2962FF)
plot(VIM, title="VI -", color=#E91E63)
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
float op_operation = decision_tree_0_ADBE_15Min_7989e3b3(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, VIP, VIM, VIP_VIM)

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


