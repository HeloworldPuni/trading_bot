//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_MA_Cross_SMA, L_Money_Flow_Index
// ID_model: SNOW_1Min_2MM0_e112927e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNOW_1Min_2MM0_e112927e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNOW_1Min_e112927e(Short_Long_Diff, MA_Cross, Long_MA, Short_MA, Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Negative_Money_Flow <= 353.079 )
		if( Positive_Money_Flow <= 98271.7 )
			if( Money_Flow_Ratio <= 1.08494 )
				if( Negative_Money_Flow_Sum <= 612638 )
					if( Short_MA <= 131.656 )
						if( Negative_Money_Flow_Sum <= 260876 )
							if( MFI <= 45.8694 )
								if( Positive_Money_Flow_Sum <= 125679 )
									ret := -0.193548
								if( Positive_Money_Flow_Sum > 125679 )
									ret := -0.776119 // sell
							if( MFI > 45.8694 )
								if( Short_Long_Diff <= -0.041932 )
									ret := 0.692308
								if( Short_Long_Diff > -0.041932 )
									ret := -0.225806
						if( Negative_Money_Flow_Sum > 260876 )
							if( Raw_Money_Flow <= 12859.9 )
								if( Positive_Money_Flow <= 11365.5 )
									ret := -0.050000
								if( Positive_Money_Flow > 11365.5 )
									ret := -0.600000
							if( Raw_Money_Flow > 12859.9 )
								if( MFI_High <= -45.8374 )
									ret := 0.314815
								if( MFI_High > -45.8374 )
									ret := 0.007264
					if( Short_MA > 131.656 )
						if( Negative_Money_Flow_Sum <= 339138 )
							if( Short_Long_Diff <= 0.060802 )
								if( Positive_Money_Flow_Sum <= 309105 )
									ret := 0.229508
								if( Positive_Money_Flow_Sum > 309105 )
									ret := -0.714286 // sell
							if( Short_Long_Diff > 0.060802 )
								if( Positive_Money_Flow <= 35666.8 )
									ret := 0.000000
								if( Positive_Money_Flow > 35666.8 )
									ret := -0.916667 // sell
						if( Negative_Money_Flow_Sum > 339138 )
							if( Positive_Money_Flow <= 3375.63 )
								if( Raw_Money_Flow <= 37493.5 )
									ret := 0.233333
								if( Raw_Money_Flow > 37493.5 )
									ret := -0.157895
							if( Positive_Money_Flow > 3375.63 )
								if( Raw_Money_Flow <= 14001.9 )
									ret := -0.285714
								if( Raw_Money_Flow > 14001.9 )
									ret := 0.511211
				if( Negative_Money_Flow_Sum > 612638 )
					if( Positive_Money_Flow <= 23556.3 )
						if( MFI_High <= -55.2265 )
							if( Money_Flow_Ratio <= 0.004445 )
								if( MA_Cross <= 29.1506 )
									ret := -0.307692
								if( MA_Cross > 29.1506 )
									ret := -1.000000 // sell
							if( Money_Flow_Ratio > 0.004445 )
								if( MFI_Low <= 1.74415 )
									ret := 0.032491
								if( MFI_Low > 1.74415 )
									ret := 0.255556
						if( MFI_High > -55.2265 )
							if( Positive_Money_Flow_Sum <= 595377 )
								if( MFI_Low <= 15.5601 )
									ret := -0.125000
								if( MFI_Low > 15.5601 )
									ret := -0.517241
							if( Positive_Money_Flow_Sum > 595377 )
								if( Short_MA <= 152.811 )
									ret := 0.143713
								if( Short_MA > 152.811 )
									ret := -0.283019
					if( Positive_Money_Flow > 23556.3 )
						if( Negative_Money_Flow_Sum <= 5.35542e+06 )
							if( Money_Flow_Ratio <= 0.191585 )
								if( Positive_Money_Flow_Sum <= 153712 )
									ret := -0.764706 // sell
								if( Positive_Money_Flow_Sum > 153712 )
									ret := -0.321429
							if( Money_Flow_Ratio > 0.191585 )
								if( Positive_Money_Flow_Sum <= 426734 )
									ret := -0.382789
								if( Positive_Money_Flow_Sum > 426734 )
									ret := -0.132308
						if( Negative_Money_Flow_Sum > 5.35542e+06 )
							if( Negative_Money_Flow_Sum <= 1.14042e+08 )
								if( Long_MA <= 162.116 )
									ret := 0.132743
								if( Long_MA > 162.116 )
									ret := -0.600000
							if( Negative_Money_Flow_Sum > 1.14042e+08 )
								if( Typical_Price <= 113.222 )
									ret := 0.400000
								if( Typical_Price > 113.222 )
									ret := -0.470588
			if( Money_Flow_Ratio > 1.08494 )
				if( MFI_High <= -24.4181 )
					if( Positive_Money_Flow_Sum <= 794881 )
						if( Positive_Money_Flow_Sum <= 361128 )
							if( Typical_Price <= 125.145 )
								if( MFI <= 52.8385 )
									ret := 0.625000
								if( MFI > 52.8385 )
									ret := 0.107143
							if( Typical_Price > 125.145 )
								if( MA_Cross <= 1.2506 )
									ret := -0.391304
								if( MA_Cross > 1.2506 )
									ret := -0.894737 // sell
						if( Positive_Money_Flow_Sum > 361128 )
							if( Raw_Money_Flow <= 68072.3 )
								if( Positive_Money_Flow_Sum <= 512861 )
									ret := -0.555556
								if( Positive_Money_Flow_Sum > 512861 )
									ret := -0.842105 // sell
							if( Raw_Money_Flow > 68072.3 )
								if( MFI_Low <= 32.7921 )
									ret := -0.750000 // sell
								if( MFI_Low > 32.7921 )
									ret := 0.000000
					if( Positive_Money_Flow_Sum > 794881 )
						if( Positive_Money_Flow_Sum <= 1.21593e+06 )
							if( Raw_Money_Flow <= 54652 )
								if( Typical_Price <= 150.943 )
									ret := -0.200000
								if( Typical_Price > 150.943 )
									ret := 0.500000
							if( Raw_Money_Flow > 54652 )
								if( Negative_Money_Flow_Sum <= 851199 )
									ret := 0.500000
								if( Negative_Money_Flow_Sum > 851199 )
									ret := 1.000000 // buy
						if( Positive_Money_Flow_Sum > 1.21593e+06 )
							if( Positive_Money_Flow_Sum <= 2.72155e+06 )
								if( Positive_Money_Flow_Sum <= 1.45735e+06 )
									ret := -1.000000 // sell
								if( Positive_Money_Flow_Sum > 1.45735e+06 )
									ret := -0.615385
							if( Positive_Money_Flow_Sum > 2.72155e+06 )
								if( Negative_Money_Flow_Sum <= 6.58835e+06 )
									ret := 0.538462
								if( Negative_Money_Flow_Sum > 6.58835e+06 )
									ret := -0.833333 // sell
				if( MFI_High > -24.4181 )
					if( Short_Long_Diff <= 0.103959 )
						if( Positive_Money_Flow <= 11265 )
							if( Positive_Money_Flow_Sum <= 2.4003e+08 )
								if( Positive_Money_Flow_Sum <= 857003 )
									ret := 0.170455
								if( Positive_Money_Flow_Sum > 857003 )
									ret := -0.076503
							if( Positive_Money_Flow_Sum > 2.4003e+08 )
								if( Short_Long_Diff <= -0.10972 )
									ret := 1.000000 // buy
								if( Short_Long_Diff > -0.10972 )
									ret := 0.000000
						if( Positive_Money_Flow > 11265 )
							if( Positive_Money_Flow_Sum <= 369343 )
								if( Money_Flow_Ratio <= 2.98198 )
									ret := -0.588235
								if( Money_Flow_Ratio > 2.98198 )
									ret := -0.071429
							if( Positive_Money_Flow_Sum > 369343 )
								if( Positive_Money_Flow <= 70073.5 )
									ret := -0.160692
								if( Positive_Money_Flow > 70073.5 )
									ret := 0.109091
					if( Short_Long_Diff > 0.103959 )
						if( Short_Long_Diff <= 1.14979 )
							if( Short_MA <= 113.047 )
								if( Short_Long_Diff <= 0.192327 )
									ret := -0.289474
								if( Short_Long_Diff > 0.192327 )
									ret := 0.421053
							if( Short_MA > 113.047 )
								if( Raw_Money_Flow <= 32072.6 )
									ret := -0.495495
								if( Raw_Money_Flow > 32072.6 )
									ret := -0.266402
						if( Short_Long_Diff > 1.14979 )
							if( Negative_Money_Flow_Sum <= 223419 )
								ret := 0.285714
							if( Negative_Money_Flow_Sum > 223419 )
								ret := 1.000000 // buy
		if( Positive_Money_Flow > 98271.7 )
			if( Typical_Price <= 171.203 )
				if( Money_Flow_Ratio <= 1.4104 )
					if( Negative_Money_Flow_Sum <= 2.05985e+07 )
						if( Positive_Money_Flow_Sum <= 2.021e+07 )
							if( Money_Flow_Ratio <= 0.960891 )
								if( Positive_Money_Flow_Sum <= 1.27826e+07 )
									ret := 0.026914
								if( Positive_Money_Flow_Sum > 1.27826e+07 )
									ret := 0.273504
							if( Money_Flow_Ratio > 0.960891 )
								if( Short_Long_Diff <= -0.052482 )
									ret := -0.114370
								if( Short_Long_Diff > -0.052482 )
									ret := -0.024467
						if( Positive_Money_Flow_Sum > 2.021e+07 )
							if( Short_Long_Diff <= -0.084969 )
								if( Money_Flow_Ratio <= 1.37506 )
									ret := 0.803279 // buy
								if( Money_Flow_Ratio > 1.37506 )
									ret := 0.000000
							if( Short_Long_Diff > -0.084969 )
								if( Typical_Price <= 114.495 )
									ret := -0.727273 // sell
								if( Typical_Price > 114.495 )
									ret := 0.227642
					if( Negative_Money_Flow_Sum > 2.05985e+07 )
						if( Typical_Price <= 125.143 )
							if( Typical_Price <= 118.104 )
								if( Positive_Money_Flow <= 1.05371e+07 )
									ret := -0.052539
								if( Positive_Money_Flow > 1.05371e+07 )
									ret := -0.470588
							if( Typical_Price > 118.104 )
								if( Short_Long_Diff <= 0.260391 )
									ret := 0.174107
								if( Short_Long_Diff > 0.260391 )
									ret := -0.833333 // sell
						if( Typical_Price > 125.143 )
							if( Money_Flow_Ratio <= 0.659156 )
								if( Positive_Money_Flow_Sum <= 1.45636e+07 )
									ret := -0.090782
								if( Positive_Money_Flow_Sum > 1.45636e+07 )
									ret := -0.391137
							if( Money_Flow_Ratio > 0.659156 )
								if( Negative_Money_Flow_Sum <= 2.3822e+07 )
									ret := -0.271186
								if( Negative_Money_Flow_Sum > 2.3822e+07 )
									ret := 0.089669
				if( Money_Flow_Ratio > 1.4104 )
					if( Raw_Money_Flow <= 799736 )
						if( Short_Long_Diff <= -0.170891 )
							if( Negative_Money_Flow_Sum <= 5.10967e+06 )
								if( Money_Flow_Ratio <= 4.40337 )
									ret := 0.590909
								if( Money_Flow_Ratio > 4.40337 )
									ret := -0.133333
							if( Negative_Money_Flow_Sum > 5.10967e+06 )
								if( Negative_Money_Flow_Sum <= 8.19213e+06 )
									ret := -0.687500
								if( Negative_Money_Flow_Sum > 8.19213e+06 )
									ret := 0.400000
						if( Short_Long_Diff > -0.170891 )
							if( Positive_Money_Flow_Sum <= 499729 )
								if( Negative_Money_Flow_Sum <= 182902 )
									ret := -0.350000
								if( Negative_Money_Flow_Sum > 182902 )
									ret := 0.656716
							if( Positive_Money_Flow_Sum > 499729 )
								if( Short_Long_Diff <= 0.265547 )
									ret := -0.008790
								if( Short_Long_Diff > 0.265547 )
									ret := -0.211765
					if( Raw_Money_Flow > 799736 )
						if( Long_MA <= 138.494 )
							if( Positive_Money_Flow <= 1.31152e+07 )
								if( Money_Flow_Ratio <= 37.2389 )
									ret := 0.124867
								if( Money_Flow_Ratio > 37.2389 )
									ret := 0.808511 // buy
							if( Positive_Money_Flow > 1.31152e+07 )
								if( Negative_Money_Flow_Sum <= 1.06947e+07 )
									ret := -0.541667
								if( Negative_Money_Flow_Sum > 1.06947e+07 )
									ret := 0.007194
						if( Long_MA > 138.494 )
							if( Short_Long_Diff <= 0.266678 )
								if( Short_Long_Diff <= -0.179026 )
									ret := 0.466667
								if( Short_Long_Diff > -0.179026 )
									ret := 0.054965
							if( Short_Long_Diff > 0.266678 )
								if( MFI <= 63.8941 )
									ret := 0.324324
								if( MFI > 63.8941 )
									ret := -0.222222
			if( Typical_Price > 171.203 )
				if( Long_MA <= 172.252 )
					if( Negative_Money_Flow_Sum <= 3.54918e+06 )
						if( Positive_Money_Flow_Sum <= 3.91818e+06 )
							ret := -0.400000
						if( Positive_Money_Flow_Sum > 3.91818e+06 )
							ret := -1.000000 // sell
					if( Negative_Money_Flow_Sum > 3.54918e+06 )
						ret := -1.000000 // sell
				if( Long_MA > 172.252 )
					if( Positive_Money_Flow_Sum <= 8.84463e+06 )
						ret := 0.250000
					if( Positive_Money_Flow_Sum > 8.84463e+06 )
						if( Long_MA <= 172.964 )
							ret := -0.750000 // sell
						if( Long_MA > 172.964 )
							ret := -1.000000 // sell
	if( Negative_Money_Flow > 353.079 )
		if( Raw_Money_Flow <= 178181 )
			if( MFI_Low <= -19.5299 )
				if( Money_Flow_Ratio <= 0.001128 )
					ret := 0.500000
				if( Money_Flow_Ratio > 0.001128 )
					if( Typical_Price <= 127.3 )
						if( Long_MA <= 114.874 )
							ret := -0.250000
						if( Long_MA > 114.874 )
							if( Negative_Money_Flow_Sum <= 4.22281e+07 )
								ret := -0.750000 // sell
							if( Negative_Money_Flow_Sum > 4.22281e+07 )
								ret := -1.000000 // sell
					if( Typical_Price > 127.3 )
						ret := 0.000000
			if( MFI_Low > -19.5299 )
				if( Positive_Money_Flow_Sum <= 242284 )
					if( Short_MA <= 126.82 )
						if( MFI_Low <= 17.4578 )
							if( Negative_Money_Flow_Sum <= 595476 )
								if( MFI <= 26.3652 )
									ret := 0.733333 // buy
								if( MFI > 26.3652 )
									ret := 0.295181
							if( Negative_Money_Flow_Sum > 595476 )
								if( Short_Long_Diff <= -1.05749 )
									ret := 1.000000 // buy
								if( Short_Long_Diff > -1.05749 )
									ret := 0.168539
						if( MFI_Low > 17.4578 )
							if( MFI <= 44.8789 )
								if( Short_Long_Diff <= -0.014138 )
									ret := -0.725000 // sell
								if( Short_Long_Diff > -0.014138 )
									ret := 0.100000
							if( MFI > 44.8789 )
								if( Short_Long_Diff <= -0.06729 )
									ret := 1.000000 // buy
								if( Short_Long_Diff > -0.06729 )
									ret := 0.016667
					if( Short_MA > 126.82 )
						if( Positive_Money_Flow_Sum <= 217079 )
							if( MFI_High <= -27.7249 )
								if( Positive_Money_Flow_Sum <= 114741 )
									ret := 0.707317 // buy
								if( Positive_Money_Flow_Sum > 114741 )
									ret := 0.404255
							if( MFI_High > -27.7249 )
								if( Short_Long_Diff <= -0.02702 )
									ret := -1.000000 // sell
								if( Short_Long_Diff > -0.02702 )
									ret := 0.000000
						if( Positive_Money_Flow_Sum > 217079 )
							if( Negative_Money_Flow <= 53190.2 )
								if( Long_MA <= 138.125 )
									ret := 0.708333 // buy
								if( Long_MA > 138.125 )
									ret := 0.947368 // buy
							if( Negative_Money_Flow > 53190.2 )
								if( Positive_Money_Flow_Sum <= 233149 )
									ret := 0.720000 // buy
								if( Positive_Money_Flow_Sum > 233149 )
									ret := 0.066667
				if( Positive_Money_Flow_Sum > 242284 )
					if( Short_MA <= 170.062 )
						if( Negative_Money_Flow_Sum <= 155376 )
							if( Positive_Money_Flow_Sum <= 507057 )
								if( Short_MA <= 118.314 )
									ret := -0.653846
								if( Short_MA > 118.314 )
									ret := 0.510638
							if( Positive_Money_Flow_Sum > 507057 )
								if( Short_MA <= 136.403 )
									ret := -0.285714
								if( Short_MA > 136.403 )
									ret := -0.772727 // sell
						if( Negative_Money_Flow_Sum > 155376 )
							if( Negative_Money_Flow_Sum <= 6.57858e+07 )
								if( Positive_Money_Flow <= 394.24 )
									ret := 0.206931
								if( Positive_Money_Flow > 394.24 )
									ret := 0.053950
							if( Negative_Money_Flow_Sum > 6.57858e+07 )
								if( Negative_Money_Flow_Sum <= 8.47694e+07 )
									ret := 0.734177 // buy
								if( Negative_Money_Flow_Sum > 8.47694e+07 )
									ret := 0.303030
					if( Short_MA > 170.062 )
						if( MFI <= 47.2495 )
							if( Negative_Money_Flow_Sum <= 3.35393e+06 )
								ret := -1.000000 // sell
							if( Negative_Money_Flow_Sum > 3.35393e+06 )
								ret := 0.000000
						if( MFI > 47.2495 )
							if( Raw_Money_Flow <= 89252.3 )
								ret := 0.250000
							if( Raw_Money_Flow > 89252.3 )
								ret := -0.500000
		if( Raw_Money_Flow > 178181 )
			if( Negative_Money_Flow_Sum <= 1.07266e+07 )
				if( Short_Long_Diff <= 1.21016 )
					if( Money_Flow_Ratio <= 2.94801 )
						if( Money_Flow_Ratio <= 0.597712 )
							if( MFI_Low <= -13.7759 )
								if( Negative_Money_Flow <= 446946 )
									ret := -0.250000
								if( Negative_Money_Flow > 446946 )
									ret := 0.686275
							if( MFI_Low > -13.7759 )
								if( Positive_Money_Flow_Sum <= 5.56133e+06 )
									ret := 0.068881
								if( Positive_Money_Flow_Sum > 5.56133e+06 )
									ret := 0.526316
						if( Money_Flow_Ratio > 0.597712 )
							if( Negative_Money_Flow <= 568103 )
								if( MFI_Low <= 20.6349 )
									ret := -0.148338
								if( MFI_Low > 20.6349 )
									ret := 0.074785
							if( Negative_Money_Flow > 568103 )
								if( Short_Long_Diff <= -0.321237 )
									ret := 0.541667
								if( Short_Long_Diff > -0.321237 )
									ret := -0.030953
					if( Money_Flow_Ratio > 2.94801 )
						if( Negative_Money_Flow_Sum <= 2.71974e+06 )
							if( Positive_Money_Flow_Sum <= 2.15814e+07 )
								if( Money_Flow_Ratio <= 5.63377 )
									ret := 0.048000
								if( Money_Flow_Ratio > 5.63377 )
									ret := -0.253425
							if( Positive_Money_Flow_Sum > 2.15814e+07 )
								if( Typical_Price <= 154.681 )
									ret := 0.681818
								if( Typical_Price > 154.681 )
									ret := -0.375000
						if( Negative_Money_Flow_Sum > 2.71974e+06 )
							if( Short_MA <= 113.157 )
								if( MFI_High <= 0.141877 )
									ret := 0.021277
								if( MFI_High > 0.141877 )
									ret := -0.488889
							if( Short_MA > 113.157 )
								if( Typical_Price <= 157.775 )
									ret := 0.282506
								if( Typical_Price > 157.775 )
									ret := -0.156627
				if( Short_Long_Diff > 1.21016 )
					if( MFI <= 98.6093 )
						if( Money_Flow_Ratio <= 61.3946 )
							ret := -1.000000 // sell
						if( Money_Flow_Ratio > 61.3946 )
							ret := -0.500000
					if( MFI > 98.6093 )
						ret := 0.000000
			if( Negative_Money_Flow_Sum > 1.07266e+07 )
				if( MFI_Low <= 43.9387 )
					if( MFI_Low <= -18.3934 )
						if( Negative_Money_Flow_Sum <= 4.60272e+07 )
							if( Negative_Money_Flow_Sum <= 3.46583e+07 )
								if( Raw_Money_Flow <= 1.50106e+06 )
									ret := 0.200000
								if( Raw_Money_Flow > 1.50106e+06 )
									ret := -0.619048
							if( Negative_Money_Flow_Sum > 3.46583e+07 )
								ret := 0.714286 // buy
						if( Negative_Money_Flow_Sum > 4.60272e+07 )
							if( Short_Long_Diff <= -0.396857 )
								if( Negative_Money_Flow <= 3.25301e+07 )
									ret := -1.000000 // sell
								if( Negative_Money_Flow > 3.25301e+07 )
									ret := -0.750000 // sell
							if( Short_Long_Diff > -0.396857 )
								if( Raw_Money_Flow <= 258273 )
									ret := -0.666667
								if( Raw_Money_Flow > 258273 )
									ret := 0.333333
					if( MFI_Low > -18.3934 )
						if( Positive_Money_Flow_Sum <= 1.60917e+08 )
							if( Negative_Money_Flow_Sum <= 1.75018e+08 )
								if( MA_Cross <= 2.33553 )
									ret := 0.087527
								if( MA_Cross > 2.33553 )
									ret := 0.373178
							if( Negative_Money_Flow_Sum > 1.75018e+08 )
								if( Typical_Price <= 157.657 )
									ret := 0.575221
								if( Typical_Price > 157.657 )
									ret := -1.000000 // sell
						if( Positive_Money_Flow_Sum > 1.60917e+08 )
							if( Negative_Money_Flow_Sum <= 3.03675e+08 )
								if( Negative_Money_Flow_Sum <= 1.50509e+08 )
									ret := -0.571429
								if( Negative_Money_Flow_Sum > 1.50509e+08 )
									ret := -0.945946 // sell
							if( Negative_Money_Flow_Sum > 3.03675e+08 )
								ret := 1.000000 // buy
				if( MFI_Low > 43.9387 )
					if( Long_MA <= 137.546 )
						if( Short_Long_Diff <= 0.533369 )
							if( Negative_Money_Flow_Sum <= 2.2512e+07 )
								if( Positive_Money_Flow_Sum <= 3.20408e+07 )
									ret := 0.355102
								if( Positive_Money_Flow_Sum > 3.20408e+07 )
									ret := -0.012500
							if( Negative_Money_Flow_Sum > 2.2512e+07 )
								if( Short_Long_Diff <= -0.224579 )
									ret := 0.888889 // buy
								if( Short_Long_Diff > -0.224579 )
									ret := 0.341176
						if( Short_Long_Diff > 0.533369 )
							if( Positive_Money_Flow_Sum <= 8.9151e+07 )
								if( Short_MA <= 131.188 )
									ret := 0.835052 // buy
								if( Short_MA > 131.188 )
									ret := 0.428571
							if( Positive_Money_Flow_Sum > 8.9151e+07 )
								if( Money_Flow_Ratio <= 3.90289 )
									ret := -0.846154 // sell
								if( Money_Flow_Ratio > 3.90289 )
									ret := 0.000000
					if( Long_MA > 137.546 )
						if( MFI <= 75.9111 )
							if( Negative_Money_Flow_Sum <= 5.05728e+07 )
								if( Negative_Money_Flow_Sum <= 1.27051e+07 )
									ret := 0.538462
								if( Negative_Money_Flow_Sum > 1.27051e+07 )
									ret := -0.008772
							if( Negative_Money_Flow_Sum > 5.05728e+07 )
								if( Money_Flow_Ratio <= 2.78971 )
									ret := 0.846154 // buy
								if( Money_Flow_Ratio > 2.78971 )
									ret := -0.400000
						if( MFI > 75.9111 )
							if( Negative_Money_Flow_Sum <= 1.62867e+07 )
								if( Typical_Price <= 145.591 )
									ret := -1.000000 // sell
								if( Typical_Price > 145.591 )
									ret := -0.500000
							if( Negative_Money_Flow_Sum > 1.62867e+07 )
								if( Short_MA <= 140.301 )
									ret := 0.750000 // buy
								if( Short_MA > 140.301 )
									ret := -0.437500
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_MA_Cross_SMA 
//@version=5
//indicator title="MA Cross", overlay=true)

shortlen = input.int(9, title="Short MA Length", minval=1)
longlen = input.int(21, title="Long MA Length", minval=1)

// Calculate the short and long simple moving averages (SMA)
Short_MA = ta.sma(close, shortlen)
Long_MA = ta.sma(close, longlen)

// Calculate the difference between short MA and long MA
Short_Long_Diff = Short_MA - Long_MA

// Identify crossover points where short MA crosses above or below the long MA
MA_Cross = ta.valuewhen(ta.crossover(Short_MA, Long_MA), Short_MA, 0)

// Plot the results
plot(Short_MA, color=color.orange, title="Short MA")
plot(Long_MA, color=color.green, title="Long MA")
plotshape(na(MA_Cross) ? na : MA_Cross, style=shape.cross, location=location.absolute, color=color.blue, title="Cross")


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
float op_operation = decision_tree_0_SNOW_1Min_e112927e(Short_Long_Diff, MA_Cross, Long_MA, Short_MA, Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow)

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


