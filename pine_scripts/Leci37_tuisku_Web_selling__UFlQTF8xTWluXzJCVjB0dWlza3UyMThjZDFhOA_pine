//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Vortex_Indicator
// ID_model: PYPL_1Min_2BV0_218cd1a8 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PYPL_1Min_2BV0_218cd1a8", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PYPL_1Min_218cd1a8(bearPower, bbm, bbp, bullPower, BBPower_Color, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( bullPower <= -0.018781 )
		if( VIP <= 1.79634 )
			if( bbm <= 0.520315 )
				if( VIM <= 1.07702 )
					if( VIM <= 1.01324 )
						if( bearPower <= -0.118881 )
							if( VIP_VIM <= -0.060899 )
								ret := -0.714286 // sell
							if( VIP_VIM > -0.060899 )
								if( VIP <= 1.05926 )
									ret := 0.377358
								if( VIP > 1.05926 )
									ret := 0.703704 // buy
						if( bearPower > -0.118881 )
							if( VIP_VIM <= 0.309574 )
								if( VIP_VIM <= 0.072418 )
									ret := 0.100592
								if( VIP_VIM > 0.072418 )
									ret := -0.295302
							if( VIP_VIM > 0.309574 )
								if( bearPower <= -0.058969 )
									ret := 0.928571 // buy
								if( bearPower > -0.058969 )
									ret := 0.200000
					if( VIM > 1.01324 )
						if( bbm <= 0.012412 )
							if( VIM <= 1.04422 )
								if( bearPower <= -0.042679 )
									ret := -0.600000
								if( bearPower > -0.042679 )
									ret := 0.000000
							if( VIM > 1.04422 )
								if( bearPower <= -0.05146 )
									ret := 1.000000 // buy
								if( bearPower > -0.05146 )
									ret := 0.736842 // buy
						if( bbm > 0.012412 )
							if( bbp <= -0.238723 )
								if( bullPower <= -0.069793 )
									ret := 0.037037
								if( bullPower > -0.069793 )
									ret := -0.839506 // sell
							if( bbp > -0.238723 )
								if( bbp <= -0.186295 )
									ret := 0.230769
								if( bbp > -0.186295 )
									ret := -0.123871
				if( VIM > 1.07702 )
					if( VIM <= 2.08659 )
						if( bearPower <= -0.197039 )
							if( bbm <= 0.09998 )
								if( VIP <= 0.60995 )
									ret := 0.053435
								if( VIP > 0.60995 )
									ret := 0.355019
							if( bbm > 0.09998 )
								if( bbp <= -0.30447 )
									ret := 0.047751
								if( bbp > -0.30447 )
									ret := 0.361765
						if( bearPower > -0.197039 )
							if( VIP_VIM <= -1.09039 )
								if( VIP <= 0.463665 )
									ret := 0.000000
								if( VIP > 0.463665 )
									ret := 0.935484 // buy
							if( VIP_VIM > -1.09039 )
								if( VIM <= 1.09494 )
									ret := 0.244681
								if( VIM > 1.09494 )
									ret := 0.066160
					if( VIM > 2.08659 )
						if( VIP <= 1.71472 )
							if( bullPower <= -0.133069 )
								if( bbm <= 0.096506 )
									ret := 0.029940
								if( bbm > 0.096506 )
									ret := 0.684211
							if( bullPower > -0.133069 )
								if( VIP <= 1.10929 )
									ret := -0.096774
								if( VIP > 1.10929 )
									ret := 0.478088
						if( VIP > 1.71472 )
							if( bullPower <= -0.104814 )
								if( VIP_VIM <= -0.788019 )
									ret := 1.000000 // buy
								if( VIP_VIM > -0.788019 )
									ret := 0.666667
							if( bullPower > -0.104814 )
								if( VIP_VIM <= -0.624582 )
									ret := -0.812500 // sell
								if( VIP_VIM > -0.624582 )
									ret := 0.142857
			if( bbm > 0.520315 )
				if( VIM <= 1.12448 )
					if( VIP_VIM <= -0.312793 )
						ret := 0.333333
					if( VIP_VIM > -0.312793 )
						ret := -1.000000 // sell
				if( VIM > 1.12448 )
					if( VIP_VIM <= -0.593488 )
						if( VIM <= 1.30382 )
							ret := -0.500000
						if( VIM > 1.30382 )
							if( VIM <= 1.41992 )
								ret := 1.000000 // buy
							if( VIM > 1.41992 )
								ret := 0.500000
					if( VIP_VIM > -0.593488 )
						ret := 1.000000 // buy
		if( VIP > 1.79634 )
			if( VIP <= 2.79049 )
				if( VIP <= 2.17152 )
					if( bullPower <= -0.237805 )
						if( VIP_VIM <= -0.577648 )
							if( bearPower <= -0.399635 )
								ret := 1.000000 // buy
							if( bearPower > -0.399635 )
								if( VIP_VIM <= -1.08428 )
									ret := 1.000000 // buy
								if( VIP_VIM > -1.08428 )
									ret := 0.333333
						if( VIP_VIM > -0.577648 )
							ret := 1.000000 // buy
					if( bullPower > -0.237805 )
						if( VIP_VIM <= -0.230265 )
							if( bbp <= -0.08526 )
								if( bullPower <= -0.029148 )
									ret := 0.288557
								if( bullPower > -0.029148 )
									ret := -0.400000
							if( bbp > -0.08526 )
								if( VIP_VIM <= -0.543939 )
									ret := 0.717949 // buy
								if( VIP_VIM > -0.543939 )
									ret := 0.176471
						if( VIP_VIM > -0.230265 )
							if( VIM <= 1.71831 )
								if( bullPower <= -0.135768 )
									ret := 0.923077 // buy
								if( bullPower > -0.135768 )
									ret := 0.051724
							if( VIM > 1.71831 )
								if( VIM <= 1.79937 )
									ret := 0.921053 // buy
								if( VIM > 1.79937 )
									ret := 0.568421
				if( VIP > 2.17152 )
					if( VIM <= 2.10467 )
						if( bbm <= 0.020955 )
							if( VIP <= 2.50092 )
								if( VIP <= 2.42377 )
									ret := 0.530612
								if( VIP > 2.42377 )
									ret := 0.956522 // buy
							if( VIP > 2.50092 )
								if( bbp <= -0.109391 )
									ret := -0.266667
								if( bbp > -0.109391 )
									ret := 0.684211
						if( bbm > 0.020955 )
							ret := -0.400000
					if( VIM > 2.10467 )
						if( VIM <= 2.2925 )
							if( bearPower <= -0.126593 )
								ret := 0.800000 // buy
							if( bearPower > -0.126593 )
								if( VIP <= 2.72274 )
									ret := -0.694915
								if( VIP > 2.72274 )
									ret := 0.500000
						if( VIM > 2.2925 )
							if( VIM <= 3.83945 )
								if( VIM <= 2.41474 )
									ret := 0.586207
								if( VIM > 2.41474 )
									ret := 0.160677
							if( VIM > 3.83945 )
								if( VIP <= 2.36717 )
									ret := 0.500000
								if( VIP > 2.36717 )
									ret := -0.636364
			if( VIP > 2.79049 )
				if( bbm <= 0.176152 )
					if( bearPower <= -0.045089 )
						if( VIM <= 5.34689 )
							if( VIP <= 5.91292 )
								if( VIP_VIM <= -1.15461 )
									ret := 0.055556
								if( VIP_VIM > -1.15461 )
									ret := 0.581736
							if( VIP > 5.91292 )
								if( VIM <= 5.04319 )
									ret := -0.200000
								if( VIM > 5.04319 )
									ret := -0.666667
						if( VIM > 5.34689 )
							if( VIP_VIM <= -0.500418 )
								if( VIM <= 8.83375 )
									ret := 0.320856
								if( VIM > 8.83375 )
									ret := 0.658892
							if( VIP_VIM > -0.500418 )
								if( bbm <= 0.02911 )
									ret := 0.369208
								if( bbm > 0.02911 )
									ret := -0.259259
					if( bearPower > -0.045089 )
						if( VIP <= 15.4994 )
							if( VIM <= 11.2656 )
								if( VIM <= 2.72662 )
									ret := 0.763158 // buy
								if( VIM > 2.72662 )
									ret := 0.303167
							if( VIM > 11.2656 )
								if( VIP <= 12.7964 )
									ret := -0.389831
								if( VIP > 12.7964 )
									ret := 0.250000
						if( VIP > 15.4994 )
							if( VIP_VIM <= 0.691112 )
								if( VIP <= 26.4513 )
									ret := 0.711538 // buy
								if( VIP > 26.4513 )
									ret := 0.391304
							if( VIP_VIM > 0.691112 )
								if( VIP_VIM <= 1.00378 )
									ret := -0.250000
								if( VIP_VIM > 1.00378 )
									ret := 0.365854
				if( bbm > 0.176152 )
					if( bullPower <= -0.992422 )
						ret := -1.000000 // sell
					if( bullPower > -0.992422 )
						ret := -0.750000 // sell
	if( bullPower > -0.018781 )
		if( VIP <= 1.51628 )
			if( bearPower <= 0.381483 )
				if( bearPower <= 0.065915 )
					if( bullPower <= 0.096857 )
						if( bbm <= 0.040538 )
							if( VIP_VIM <= -0.12695 )
								if( bbp <= -0.02536 )
									ret := -0.038285
								if( bbp > -0.02536 )
									ret := 0.092559
							if( VIP_VIM > -0.12695 )
								if( bearPower <= -0.038153 )
									ret := -0.169978
								if( bearPower > -0.038153 )
									ret := -0.004132
						if( bbm > 0.040538 )
							if( VIP_VIM <= -0.665156 )
								if( bearPower <= -0.247007 )
									ret := 0.976190 // buy
								if( bearPower > -0.247007 )
									ret := 0.358491
							if( VIP_VIM > -0.665156 )
								if( bearPower <= -0.257591 )
									ret := -0.304054
								if( bearPower > -0.257591 )
									ret := 0.048271
					if( bullPower > 0.096857 )
						if( bbm <= 0.73939 )
							if( VIP <= 1.07785 )
								if( VIP_VIM <= 0.044796 )
									ret := 0.104463
								if( VIP_VIM > 0.044796 )
									ret := -0.119710
							if( VIP > 1.07785 )
								if( VIP_VIM <= 0.181099 )
									ret := 0.333890
								if( VIP_VIM > 0.181099 )
									ret := 0.098183
						if( bbm > 0.73939 )
							if( bearPower <= -3.52112 )
								if( VIM <= 0.950898 )
									ret := -1.000000 // sell
								if( VIM > 0.950898 )
									ret := -0.750000 // sell
							if( bearPower > -3.52112 )
								if( bullPower <= 0.142931 )
									ret := 0.076923
								if( bullPower > 0.142931 )
									ret := 0.851064 // buy
				if( bearPower > 0.065915 )
					if( bbm <= 0.077968 )
						if( VIP_VIM <= 0.547316 )
							if( VIP <= 1.48112 )
								if( bbm <= 0.009424 )
									ret := -0.425121
								if( bbm > 0.009424 )
									ret := -0.155797
							if( VIP > 1.48112 )
								if( VIM <= 1.26889 )
									ret := -0.200000
								if( VIM > 1.26889 )
									ret := 0.827586 // buy
						if( VIP_VIM > 0.547316 )
							if( VIP_VIM <= 0.772762 )
								if( bbp <= 0.172908 )
									ret := -0.308642
								if( bbp > 0.172908 )
									ret := 0.102778
							if( VIP_VIM > 0.772762 )
								if( bbp <= 0.28265 )
									ret := -0.061674
								if( bbp > 0.28265 )
									ret := -0.547170
					if( bbm > 0.077968 )
						if( VIM <= 0.49369 )
							if( VIM <= 0.464951 )
								if( bullPower <= 0.185983 )
									ret := 1.000000 // buy
								if( bullPower > 0.185983 )
									ret := -0.071429
							if( VIM > 0.464951 )
								if( bullPower <= 0.211112 )
									ret := 0.750000 // buy
								if( bullPower > 0.211112 )
									ret := 1.000000 // buy
						if( VIM > 0.49369 )
							if( VIP <= 1.50319 )
								if( VIM <= 0.574351 )
									ret := -0.321839
								if( VIM > 0.574351 )
									ret := 0.037921
							if( VIP > 1.50319 )
								if( bullPower <= 0.313262 )
									ret := -0.500000
								if( bullPower > 0.313262 )
									ret := -1.000000 // sell
			if( bearPower > 0.381483 )
				if( VIP_VIM <= 0.974171 )
					if( bearPower <= 1.02056 )
						if( VIP <= 1.37401 )
							if( VIP <= 1.1786 )
								if( bearPower <= 0.577356 )
									ret := 1.000000 // buy
								if( bearPower > 0.577356 )
									ret := 0.727273 // buy
							if( VIP > 1.1786 )
								if( VIM <= 0.793866 )
									ret := -0.222222
								if( VIM > 0.793866 )
									ret := 1.000000 // buy
						if( VIP > 1.37401 )
							if( VIM <= 0.542914 )
								if( VIM <= 0.541528 )
									ret := 0.916667 // buy
								if( VIM > 0.541528 )
									ret := 0.000000
							if( VIM > 0.542914 )
								if( VIP_VIM <= 0.728391 )
									ret := 0.750000 // buy
								if( VIP_VIM > 0.728391 )
									ret := 0.983051 // buy
					if( bearPower > 1.02056 )
						if( bullPower <= 1.81714 )
							ret := -1.000000 // sell
						if( bullPower > 1.81714 )
							ret := 0.666667
				if( VIP_VIM > 0.974171 )
					ret := -1.000000 // sell
		if( VIP > 1.51628 )
			if( bbp <= 0.113723 )
				if( bbp <= -0.006656 )
					if( VIP_VIM <= -0.579109 )
						if( VIM <= 2.6829 )
							if( bearPower <= -0.071837 )
								ret := 1.000000 // buy
							if( bearPower > -0.071837 )
								if( VIP_VIM <= -0.821233 )
									ret := 0.944444 // buy
								if( VIP_VIM > -0.821233 )
									ret := 0.000000
						if( VIM > 2.6829 )
							if( bbp <= -0.019654 )
								if( VIP_VIM <= -1.00833 )
									ret := 0.261261
								if( VIP_VIM > -1.00833 )
									ret := 0.515528
							if( bbp > -0.019654 )
								if( VIP_VIM <= -1.38267 )
									ret := 0.434783
								if( VIP_VIM > -1.38267 )
									ret := -0.078125
					if( VIP_VIM > -0.579109 )
						if( VIP_VIM <= -0.292657 )
							if( VIM <= 4.87126 )
								if( VIP <= 2.73885 )
									ret := -0.018018
								if( VIP > 2.73885 )
									ret := -0.584906
							if( VIM > 4.87126 )
								if( VIP_VIM <= -0.379588 )
									ret := 0.415094
								if( VIP_VIM > -0.379588 )
									ret := -0.333333
						if( VIP_VIM > -0.292657 )
							if( VIM <= 2.33169 )
								if( VIP <= 2.97826 )
									ret := 0.351406
								if( VIP > 2.97826 )
									ret := -0.684211
							if( VIM > 2.33169 )
								if( bbp <= -0.102111 )
									ret := 0.857143 // buy
								if( bbp > -0.102111 )
									ret := 0.136150
				if( bbp > -0.006656 )
					if( VIP_VIM <= 0.885916 )
						if( bullPower <= 0.021698 )
							if( VIP_VIM <= -1.27378 )
								if( VIM <= 10.0608 )
									ret := -0.395349
								if( VIM > 10.0608 )
									ret := -0.075000
							if( VIP_VIM > -1.27378 )
								if( VIP_VIM <= 0.555074 )
									ret := 0.028146
								if( VIP_VIM > 0.555074 )
									ret := 0.201087
						if( bullPower > 0.021698 )
							if( VIP_VIM <= 0.234764 )
								if( VIP_VIM <= -0.711982 )
									ret := -0.219072
								if( VIP_VIM > -0.711982 )
									ret := 0.010279
							if( VIP_VIM > 0.234764 )
								if( VIP_VIM <= 0.62355 )
									ret := -0.239398
								if( VIP_VIM > 0.62355 )
									ret := -0.045845
					if( VIP_VIM > 0.885916 )
						if( VIM <= 1.28775 )
							if( bbm <= 0.039065 )
								if( VIM <= 0.691291 )
									ret := 0.000000
								if( VIM > 0.691291 )
									ret := 0.741935 // buy
							if( bbm > 0.039065 )
								ret := -0.333333
						if( VIM > 1.28775 )
							if( VIP <= 3.34912 )
								if( VIM <= 1.87868 )
									ret := -0.054348
								if( VIM > 1.87868 )
									ret := -0.625000
							if( VIP > 3.34912 )
								if( VIP <= 4.18456 )
									ret := 0.474747
								if( VIP > 4.18456 )
									ret := 0.084000
			if( bbp > 0.113723 )
				if( VIP <= 3.87268 )
					if( bearPower <= 0.144131 )
						if( VIP_VIM <= 0.71956 )
							if( bearPower <= -0.100374 )
								ret := 1.000000 // buy
							if( bearPower > -0.100374 )
								if( bbm <= 0.009927 )
									ret := -0.493569
								if( bbm > 0.009927 )
									ret := -0.291525
						if( VIP_VIM > 0.71956 )
							if( VIP <= 1.8677 )
								if( VIM <= 0.936045 )
									ret := 0.157895
								if( VIM > 0.936045 )
									ret := 0.944444 // buy
							if( VIP > 1.8677 )
								if( VIP_VIM <= 1.44481 )
									ret := -0.287009
								if( VIP_VIM > 1.44481 )
									ret := 0.512821
					if( bearPower > 0.144131 )
						if( VIP_VIM <= 1.19943 )
							if( bullPower <= 0.6163 )
								if( bbm <= 0.112521 )
									ret := -0.629526
								if( bbm > 0.112521 )
									ret := -0.252747
							if( bullPower > 0.6163 )
								if( bbp <= 0.94114 )
									ret := -0.500000
								if( bbp > 0.94114 )
									ret := -0.976744 // sell
						if( VIP_VIM > 1.19943 )
							if( VIM <= 0.77187 )
								if( bbp <= 0.713203 )
									ret := -0.500000
								if( bbp > 0.713203 )
									ret := -1.000000 // sell
							if( VIM > 0.77187 )
								if( VIP <= 2.15672 )
									ret := 1.000000 // buy
								if( VIP > 2.15672 )
									ret := -0.125000
				if( VIP > 3.87268 )
					if( VIP_VIM <= 0.989559 )
						if( VIM <= 4.57553 )
							if( bearPower <= 0.133136 )
								if( VIP_VIM <= 0.876772 )
									ret := 0.232323
								if( VIP_VIM > 0.876772 )
									ret := -0.590909
							if( bearPower > 0.133136 )
								if( VIM <= 3.83795 )
									ret := -0.857143 // sell
								if( VIM > 3.83795 )
									ret := -0.212121
						if( VIM > 4.57553 )
							if( VIM <= 10.1987 )
								if( VIP_VIM <= 0.015601 )
									ret := -0.382716
								if( VIP_VIM > 0.015601 )
									ret := -0.625984
							if( VIM > 10.1987 )
								if( VIM <= 15.9906 )
									ret := 0.013699
								if( VIM > 15.9906 )
									ret := -0.360927
					if( VIP_VIM > 0.989559 )
						if( VIP <= 33.8492 )
							if( bearPower <= 0.282518 )
								if( VIP <= 4.48279 )
									ret := -0.411765
								if( VIP > 4.48279 )
									ret := 0.085837
							if( bearPower > 0.282518 )
								if( bullPower <= 0.496773 )
									ret := 0.727273 // buy
								if( bullPower > 0.496773 )
									ret := 0.111111
						if( VIP > 33.8492 )
							if( bullPower <= 0.151235 )
								if( bbp <= 0.139101 )
									ret := 0.363636
								if( bbp > 0.139101 )
									ret := -0.222222
							if( bullPower > 0.151235 )
								if( bullPower <= 0.187471 )
									ret := -1.000000 // sell
								if( bullPower > 0.187471 )
									ret := -0.500000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Bull_Bear_Power 
//@version=5
//indicator "Bull Bear Power", shorttitle="BBP")
lengthInput = input.int(13, title="Length")
bullPower = high - ta.ema(close, lengthInput)
bearPower = low - ta.ema(close, lengthInput)
bbp = bullPower + bearPower

bbm = bullPower - bearPower

plot(bbp, color = bbp >= 0 ? #089981 : #f23645, title="BBPower", style = plot.style_columns)
hline(0, "Zero line")

BBPower_Color = bbp >= 0  ? 1: 0


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
float op_operation = decision_tree_0_PYPL_1Min_218cd1a8(bearPower, bbm, bbp, bullPower, BBPower_Color, VIP, VIP_VIM, VIM)

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


