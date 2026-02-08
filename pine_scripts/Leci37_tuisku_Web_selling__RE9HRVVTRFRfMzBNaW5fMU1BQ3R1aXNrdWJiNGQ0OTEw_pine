//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: DOGEUSDT_30Min_1MAC_bb4d4910 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DOGEUSDT_30Min_1MAC_bb4d4910", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DOGEUSDT_30Min_bb4d4910(macd, macd_IsBelowInt, signal, histB_IsUpInt, macd_IsAboveInt, histB_IsDownInt, histA_IsUpInt, hist, histA_IsDownInt)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( macd <= -0.001805 )
		if( macd <= -0.002737 )
			if( histB_IsDownInt <= 0.5 )
				if( hist <= 0.011436 )
					if( signal <= -0.012823 )
						if( hist <= -0.005984 )
							if( signal <= -0.019576 )
								if( signal <= -0.023672 )
									ret := -1.000000 // sell
								if( signal > -0.023672 )
									ret := 0.600000
							if( signal > -0.019576 )
								ret := -1.000000 // sell
						if( hist > -0.005984 )
							if( macd <= -0.018175 )
								if( macd <= -0.019539 )
									ret := 1.000000 // buy
								if( macd > -0.019539 )
									ret := 0.833333 // buy
							if( macd > -0.018175 )
								if( hist <= 0.006874 )
									ret := 0.240223
								if( hist > 0.006874 )
									ret := -0.666667
					if( signal > -0.012823 )
						if( hist <= 0.001301 )
							if( signal <= -0.002321 )
								if( signal <= -0.009503 )
									ret := -0.381679
								if( signal > -0.009503 )
									ret := 0.061893
							if( signal > -0.002321 )
								if( macd <= -0.006706 )
									ret := 0.714286 // buy
								if( macd > -0.006706 )
									ret := -0.380208
						if( hist > 0.001301 )
							if( macd <= -0.00969 )
								if( macd <= -0.010126 )
									ret := 1.000000 // buy
								if( macd > -0.010126 )
									ret := 0.750000 // buy
							if( macd > -0.00969 )
								if( hist <= 0.002247 )
									ret := -0.581152
								if( hist > 0.002247 )
									ret := -0.111111
				if( hist > 0.011436 )
					ret := 1.000000 // buy
			if( histB_IsDownInt > 0.5 )
				if( signal <= -0.003145 )
					if( macd <= -0.037848 )
						if( signal <= -0.037435 )
							ret := -0.250000
						if( signal > -0.037435 )
							ret := -1.000000 // sell
					if( macd > -0.037848 )
						if( hist <= -0.004132 )
							if( macd <= -0.008356 )
								if( macd <= -0.019704 )
									ret := 0.625000
								if( macd > -0.019704 )
									ret := 0.927711 // buy
							if( macd > -0.008356 )
								ret := 0.285714
						if( hist > -0.004132 )
							if( macd <= -0.005693 )
								if( signal <= -0.014797 )
									ret := -1.000000 // sell
								if( signal > -0.014797 )
									ret := 0.292683
							if( macd > -0.005693 )
								if( hist <= -0.000128 )
									ret := 0.772358 // buy
								if( hist > -0.000128 )
									ret := 0.100000
				if( signal > -0.003145 )
					if( macd <= -0.006377 )
						if( signal <= -0.00278 )
							ret := -0.250000
						if( signal > -0.00278 )
							ret := -1.000000 // sell
					if( macd > -0.006377 )
						if( signal <= -0.002276 )
							if( macd <= -0.00311 )
								if( macd <= -0.005195 )
									ret := 0.500000
								if( macd > -0.005195 )
									ret := -0.102564
							if( macd > -0.00311 )
								if( hist <= -0.000639 )
									ret := -0.750000 // sell
								if( hist > -0.000639 )
									ret := -1.000000 // sell
						if( signal > -0.002276 )
							if( hist <= -0.001382 )
								if( signal <= -0.002008 )
									ret := -0.428571
								if( signal > -0.002008 )
									ret := 0.400000
							if( hist > -0.001382 )
								if( hist <= -0.000687 )
									ret := 0.801980 // buy
								if( hist > -0.000687 )
									ret := -0.800000 // sell
		if( macd > -0.002737 )
			if( signal <= -0.001117 )
				if( signal <= -0.002314 )
					if( histB_IsDownInt <= 0.5 )
						if( histA_IsDownInt <= 0.5 )
							if( macd <= -0.002437 )
								if( signal <= -0.002345 )
									ret := 0.495868
								if( signal > -0.002345 )
									ret := -1.000000 // sell
							if( macd > -0.002437 )
								if( macd <= -0.001833 )
									ret := -0.077739
								if( macd > -0.001833 )
									ret := 0.636364
						if( histA_IsDownInt > 0.5 )
							if( hist <= 0.000312 )
								if( signal <= -0.00241 )
									ret := 0.975000 // buy
								if( signal > -0.00241 )
									ret := 0.571429
							if( hist > 0.000312 )
								if( signal <= -0.00265 )
									ret := 0.406250
								if( signal > -0.00265 )
									ret := -0.176471
					if( histB_IsDownInt > 0.5 )
						if( signal <= -0.002346 )
							ret := -0.500000
						if( signal > -0.002346 )
							ret := -1.000000 // sell
				if( signal > -0.002314 )
					if( histB_IsUpInt <= 0.5 )
						if( signal <= -0.002103 )
							if( hist <= 0.000329 )
								if( hist <= 5.8e-05 )
									ret := 0.925373 // buy
								if( hist > 5.8e-05 )
									ret := 0.653846
							if( hist > 0.000329 )
								if( histA_IsUpInt <= 0.5 )
									ret := -0.833333 // sell
								if( histA_IsUpInt > 0.5 )
									ret := 0.600000
						if( signal > -0.002103 )
							if( hist <= -0.001307 )
								ret := -0.714286 // sell
							if( hist > -0.001307 )
								if( signal <= -0.002027 )
									ret := -0.045455
								if( signal > -0.002027 )
									ret := 0.466357
					if( histB_IsUpInt > 0.5 )
						if( macd <= -0.002523 )
							if( signal <= -0.002247 )
								ret := -0.500000
							if( signal > -0.002247 )
								if( macd <= -0.002582 )
									ret := 0.363636
								if( macd > -0.002582 )
									ret := 0.833333 // buy
						if( macd > -0.002523 )
							if( signal <= -0.001381 )
								if( hist <= -0.000845 )
									ret := -0.545455
								if( hist > -0.000845 )
									ret := 0.152805
							if( signal > -0.001381 )
								if( hist <= -0.001026 )
									ret := -0.227273
								if( hist > -0.001026 )
									ret := 0.551402
			if( signal > -0.001117 )
				if( hist <= -0.00163 )
					if( histB_IsDownInt <= 0.5 )
						if( macd <= -0.002014 )
							if( macd <= -0.002564 )
								ret := -0.600000
							if( macd > -0.002564 )
								if( signal <= 0.00118 )
									ret := -0.090909
								if( signal > 0.00118 )
									ret := 0.666667
						if( macd > -0.002014 )
							ret := -1.000000 // sell
					if( histB_IsDownInt > 0.5 )
						if( signal <= 7.6e-05 )
							if( macd <= -0.002324 )
								if( signal <= -0.000904 )
									ret := 0.000000
								if( signal > -0.000904 )
									ret := 0.937500 // buy
							if( macd > -0.002324 )
								if( hist <= -0.001913 )
									ret := -0.600000
								if( hist > -0.001913 )
									ret := 0.333333
						if( signal > 7.6e-05 )
							if( macd <= -0.002151 )
								ret := 0.750000 // buy
							if( macd > -0.002151 )
								ret := 1.000000 // buy
				if( hist > -0.00163 )
					if( macd <= -0.00195 )
						if( signal <= -0.000886 )
							if( hist <= -0.001218 )
								if( signal <= -0.001069 )
									ret := -0.714286 // sell
								if( signal > -0.001069 )
									ret := -0.250000
							if( hist > -0.001218 )
								if( histB_IsDownInt <= 0.5 )
									ret := -0.375000
								if( histB_IsDownInt > 0.5 )
									ret := 0.666667
						if( signal > -0.000886 )
							if( macd <= -0.002143 )
								if( histB_IsUpInt <= 0.5 )
									ret := -0.800000 // sell
								if( histB_IsUpInt > 0.5 )
									ret := 0.555556
							if( macd > -0.002143 )
								if( signal <= -0.000819 )
									ret := -0.538462
								if( signal > -0.000819 )
									ret := -0.846154 // sell
					if( macd > -0.00195 )
						if( hist <= -0.000762 )
							if( hist <= -0.001184 )
								if( signal <= -0.000564 )
									ret := -0.500000
								if( signal > -0.000564 )
									ret := 0.000000
							if( hist > -0.001184 )
								if( macd <= -0.00187 )
									ret := -0.071429
								if( macd > -0.00187 )
									ret := 0.555556
						if( hist > -0.000762 )
							ret := -0.833333 // sell
	if( macd > -0.001805 )
		if( hist <= -0.000607 )
			if( signal <= 4e-06 )
				if( hist <= -0.001001 )
					if( hist <= -0.001102 )
						if( macd <= -0.001215 )
							if( hist <= -0.001106 )
								if( macd <= -0.001683 )
									ret := 0.300000
								if( macd > -0.001683 )
									ret := -0.152174
							if( hist > -0.001106 )
								ret := 1.000000 // buy
						if( macd > -0.001215 )
							if( macd <= -0.001186 )
								ret := 1.000000 // buy
							if( macd > -0.001186 )
								ret := 0.750000 // buy
					if( hist > -0.001102 )
						if( histB_IsUpInt <= 0.5 )
							if( hist <= -0.001043 )
								if( macd <= -0.001513 )
									ret := -1.000000 // sell
								if( macd > -0.001513 )
									ret := -0.600000
							if( hist > -0.001043 )
								if( signal <= -0.000299 )
									ret := 0.000000
								if( signal > -0.000299 )
									ret := -0.666667
						if( histB_IsUpInt > 0.5 )
							if( hist <= -0.001061 )
								ret := -0.600000
							if( hist > -0.001061 )
								ret := 0.333333
				if( hist > -0.001001 )
					if( signal <= -0.000522 )
						if( hist <= -0.000715 )
							if( signal <= -0.000818 )
								if( hist <= -0.000764 )
									ret := -0.208333
								if( hist > -0.000764 )
									ret := -0.666667
							if( signal > -0.000818 )
								if( macd <= -0.001646 )
									ret := 0.541667
								if( macd > -0.001646 )
									ret := 0.125000
						if( hist > -0.000715 )
							if( signal <= -0.000749 )
								if( macd <= -0.001492 )
									ret := 0.415385
								if( macd > -0.001492 )
									ret := 0.933333 // buy
							if( signal > -0.000749 )
								if( hist <= -0.000653 )
									ret := 0.208333
								if( hist > -0.000653 )
									ret := -0.347826
					if( signal > -0.000522 )
						if( signal <= -0.000343 )
							if( signal <= -0.000436 )
								if( signal <= -0.000488 )
									ret := 0.675000
								if( signal > -0.000488 )
									ret := 0.352941
							if( signal > -0.000436 )
								if( signal <= -0.000428 )
									ret := 1.000000 // buy
								if( signal > -0.000428 )
									ret := 0.671053
						if( signal > -0.000343 )
							if( signal <= -0.000295 )
								if( histB_IsUpInt <= 0.5 )
									ret := -0.318182
								if( histB_IsUpInt > 0.5 )
									ret := 0.500000
							if( signal > -0.000295 )
								if( macd <= -0.000861 )
									ret := 0.529801
								if( macd > -0.000861 )
									ret := 0.246575
			if( signal > 4e-06 )
				if( hist <= -0.001905 )
					if( macd <= 0.006634 )
						if( macd <= -0.001602 )
							if( hist <= -0.00266 )
								ret := -0.500000
							if( hist > -0.00266 )
								ret := -1.000000 // sell
						if( macd > -0.001602 )
							if( hist <= -0.002903 )
								if( hist <= -0.003418 )
									ret := 0.564815
								if( hist > -0.003418 )
									ret := 0.857143 // buy
							if( hist > -0.002903 )
								if( macd <= 0.001456 )
									ret := 0.630769
								if( macd > 0.001456 )
									ret := 0.173077
					if( macd > 0.006634 )
						if( signal <= 0.012728 )
							if( signal <= 0.010901 )
								if( macd <= 0.007105 )
									ret := -0.625000
								if( macd > 0.007105 )
									ret := 0.176471
							if( signal > 0.010901 )
								if( macd <= 0.008257 )
									ret := -1.000000 // sell
								if( macd > 0.008257 )
									ret := -0.636364
						if( signal > 0.012728 )
							if( signal <= 0.016091 )
								if( hist <= -0.005396 )
									ret := 0.142857
								if( hist > -0.005396 )
									ret := 0.969697 // buy
							if( signal > 0.016091 )
								if( signal <= 0.019148 )
									ret := -0.428571
								if( signal > 0.019148 )
									ret := 0.375000
				if( hist > -0.001905 )
					if( macd <= 0.013252 )
						if( hist <= -0.000893 )
							if( macd <= 0.005292 )
								if( signal <= 0.004771 )
									ret := 0.058402
								if( signal > 0.004771 )
									ret := 0.419643
							if( macd > 0.005292 )
								if( signal <= 0.007002 )
									ret := -0.928571 // sell
								if( signal > 0.007002 )
									ret := -0.144330
						if( hist > -0.000893 )
							if( macd <= 0.001695 )
								if( macd <= 0.001107 )
									ret := 0.190533
								if( macd > 0.001107 )
									ret := -0.147287
							if( macd > 0.001695 )
								if( macd <= 0.00195 )
									ret := 0.787234 // buy
								if( macd > 0.00195 )
									ret := 0.333333
					if( macd > 0.013252 )
						if( hist <= -0.001153 )
							if( macd <= 0.023226 )
								if( signal <= 0.015782 )
									ret := 0.888889 // buy
								if( signal > 0.015782 )
									ret := -0.500000
							if( macd > 0.023226 )
								ret := 1.000000 // buy
						if( hist > -0.001153 )
							ret := 1.000000 // buy
		if( hist > -0.000607 )
			if( hist <= 0.006575 )
				if( hist <= 0.000354 )
					if( signal <= -9.1e-05 )
						if( signal <= -0.001168 )
							if( signal <= -0.001388 )
								if( hist <= -8.9e-05 )
									ret := -0.290541
								if( hist > -8.9e-05 )
									ret := 0.100711
							if( signal > -0.001388 )
								if( hist <= -0.00048 )
									ret := 0.641026
								if( hist > -0.00048 )
									ret := 0.179063
						if( signal > -0.001168 )
							if( hist <= 0.000274 )
								if( macd <= -0.001203 )
									ret := -0.145374
								if( macd > -0.001203 )
									ret := 0.020239
							if( hist > 0.000274 )
								if( macd <= -0.000713 )
									ret := -0.491525
								if( macd > -0.000713 )
									ret := -0.137500
					if( signal > -9.1e-05 )
						if( signal <= -7.8e-05 )
							if( macd <= -0.000104 )
								if( macd <= -0.000195 )
									ret := 0.242424
								if( macd > -0.000195 )
									ret := -0.109375
							if( macd > -0.000104 )
								if( hist <= 4.3e-05 )
									ret := 0.433071
								if( hist > 4.3e-05 )
									ret := 0.042553
						if( signal > -7.8e-05 )
							if( hist <= 0.000244 )
								if( hist <= -0.000424 )
									ret := 0.135301
								if( hist > -0.000424 )
									ret := 0.042497
							if( hist > 0.000244 )
								if( macd <= 0.001897 )
									ret := 0.171601
								if( macd > 0.001897 )
									ret := -0.190955
				if( hist > 0.000354 )
					if( signal <= 0.002691 )
						if( histA_IsDownInt <= 0.5 )
							if( signal <= -0.001292 )
								if( signal <= -0.002049 )
									ret := -0.172840
								if( signal > -0.002049 )
									ret := 0.118227
							if( signal > -0.001292 )
								if( macd <= 0.003542 )
									ret := -0.123850
								if( macd > 0.003542 )
									ret := -0.433071
						if( histA_IsDownInt > 0.5 )
							if( hist <= 0.00077 )
								if( macd <= -0.001551 )
									ret := -0.684211
								if( macd > -0.001551 )
									ret := -0.019328
							if( hist > 0.00077 )
								if( macd <= 0.000384 )
									ret := 0.393258
								if( macd > 0.000384 )
									ret := -0.011553
					if( signal > 0.002691 )
						if( macd <= 0.004177 )
							if( macd <= 0.003208 )
								if( hist <= 0.000371 )
									ret := -0.800000 // sell
								if( hist > 0.000371 )
									ret := 0.250000
							if( macd > 0.003208 )
								if( hist <= 0.000726 )
									ret := 0.333333
								if( hist > 0.000726 )
									ret := 0.630952
						if( macd > 0.004177 )
							if( macd <= 0.017228 )
								if( signal <= 0.004227 )
									ret := 0.216374
								if( signal > 0.004227 )
									ret := -0.126010
							if( macd > 0.017228 )
								if( macd <= 0.028701 )
									ret := 0.486486
								if( macd > 0.028701 )
									ret := -0.428571
			if( hist > 0.006575 )
				if( hist <= 0.008579 )
					if( hist <= 0.008175 )
						if( signal <= 0.007827 )
							if( signal <= -0.006548 )
								ret := -0.500000
							if( signal > -0.006548 )
								if( histA_IsUpInt <= 0.5 )
									ret := -0.714286 // sell
								if( histA_IsUpInt > 0.5 )
									ret := -1.000000 // sell
						if( signal > 0.007827 )
							if( signal <= 0.01463 )
								if( signal <= 0.010529 )
									ret := -0.428571
								if( signal > 0.010529 )
									ret := 0.600000
							if( signal > 0.01463 )
								if( macd <= 0.029946 )
									ret := -0.666667
								if( macd > 0.029946 )
									ret := -1.000000 // sell
					if( hist > 0.008175 )
						if( signal <= 0.013357 )
							ret := -0.250000
						if( signal > 0.013357 )
							ret := 0.400000
				if( hist > 0.008579 )
					if( histA_IsUpInt <= 0.5 )
						if( hist <= 0.010169 )
							ret := -1.000000 // sell
						if( hist > 0.010169 )
							if( signal <= 0.006375 )
								ret := -1.000000 // sell
							if( signal > 0.006375 )
								ret := 0.500000
					if( histA_IsUpInt > 0.5 )
						if( macd <= 0.011354 )
							if( signal <= -0.004446 )
								ret := -0.750000 // sell
							if( signal > -0.004446 )
								ret := -0.500000
						if( macd > 0.011354 )
							if( hist <= 0.011823 )
								ret := -1.000000 // sell
							if( hist > 0.011823 )
								ret := -0.800000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator MACD_ULT_MTF 
//@version=5
//indicator title="CM_MacD_Ult_MTF", shorttitle="CM_Ult_MacD_MTF", overlay=false)

source = close
useCurrentRes = input(true, title="Use Current Chart Resolution?")
resCustom = input.timeframe(title="Use Different Timeframe? Uncheck Box Above", defval="60")
smd = input(true, title="Show MacD & Signal Line? Also Turn Off Dots Below")
sd = input(true, title="Show Dots When MacD Crosses Signal Line?")
sh = input(true, title="Show Histogram?")
macd_colorChange = input(true,title="Change MacD Line Color-Signal Line Cross?")
hist_colorChange = input(true,title="MacD Histogram 4 Colors?")

res = useCurrentRes ? timeframe.period : resCustom

fastLength = input.int(12, minval=1)
slowLength = input.int(26, minval=1)
signalLength = input.int(9, minval=1)

fastMA = ta.ema(source, fastLength)
slowMA = ta.ema(source, slowLength)

macd = fastMA - slowMA
signal = ta.sma(macd, signalLength)
hist = macd - signal

outMacD = request.security(syminfo.tickerid, res, macd)
outSignal = request.security(syminfo.tickerid, res, signal)
outHist = request.security(syminfo.tickerid, res, hist)

histA_IsUp = outHist > outHist[1] and outHist > 0
histA_IsDown = outHist < outHist[1] and outHist > 0
histB_IsDown = outHist < outHist[1] and outHist <= 0
histB_IsUp = outHist > outHist[1] and outHist <= 0

// MacD Color Definitions
macd_IsAbove = outMacD >= outSignal
macd_IsBelow = outMacD < outSignal

plot_color = hist_colorChange ? histA_IsUp ? color.aqua : histA_IsDown ? color.blue : histB_IsDown ? color.red : histB_IsUp ? color.maroon : color.yellow : color.gray
macd_color = macd_colorChange ? macd_IsAbove ? color.lime : color.red : color.red
signal_color = macd_colorChange ? macd_IsAbove ? color.yellow : color.yellow : color.lime

circleYPosition = outSignal

plot(smd and outMacD ? outMacD : na, title="MACD", color=macd_color, linewidth=4)
plot(smd and outSignal ? outSignal : na, title="Signal Line", color=signal_color, style=plot.style_line, linewidth=2)
plot(sh and outHist ? outHist : na, title="Histogram", color=plot_color, style=plot.style_histogram, linewidth=4)
plot(sd and ta.cross(outMacD, outSignal) ? circleYPosition : na, title="Cross", style=plot.style_circles, linewidth=4, color=macd_color)
hline(0, '0 Line', linestyle=hline.style_solid, linewidth=2, color=color.white)

histA_IsUpInt = histA_IsUp ? 1: 0
histA_IsDownInt = histA_IsDown ? 1: 0
histB_IsDownInt = histB_IsDown ? 1: 0
histB_IsUpInt = histB_IsUp ? 1: 0
macd_IsAboveInt = macd_IsAbove ? 1: 0
macd_IsBelowInt = macd_IsBelow ? 1: 0

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
float op_operation = decision_tree_0_DOGEUSDT_30Min_bb4d4910(macd, macd_IsBelowInt, signal, histB_IsUpInt, macd_IsAboveInt, histB_IsDownInt, histA_IsUpInt, hist, histA_IsDownInt)

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


