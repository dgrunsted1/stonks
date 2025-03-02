import yfinance as yahooFinance
import pandas as pd
import matplotlib.pyplot as plt
import math

stonks = {
    "david": ["wh","gbtc","shop","kc","gap","intc", "fresx", "hmsfx", "akrex", "nvda", "nlr"]
}
data = []

for stock in stonks["david"]:
    data.append(yahooFinance.Ticker(stock))

pd.set_option('display.max_rows', None)
# Let us get historical stock prices for Facebook 
# covering the past few years.
# max->maximum number of daily prices available 
# for Facebook.
# Valid options are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 
# 5y, 10y and ytd.
num_stocks = len(data)
cols = 2
rows = math.ceil(num_stocks / cols)

# Create a figure with a grid of subplots
fig, axs = plt.subplots(rows, cols, figsize=(12, 2 * rows))
axs = axs.flatten()

for cnt, curr in enumerate(data):
    historical_data = curr.history(period="5y", interval="1wk")
    axs[cnt].plot(historical_data.index, historical_data['Close'], label='Close', color='blue')
    axs[cnt].plot(historical_data.index, historical_data['Open'], label='Open', color='red')
    axs[cnt].plot(historical_data.index, historical_data['High'], label='High', color='green')
    axs[cnt].plot(historical_data.index, historical_data['Low'], label='Low', color='grey')
    axs[cnt].set_title(f"{cnt}:    {curr.info['shortName']}")
    axs[cnt].set_xlabel('Date')
    mean_price = historical_data['Close'].mean()
    range = mean_price * .35
    # axs[cnt].set_ylim(mean_price - range, mean_price + range) 
    axs[cnt].set_ylabel('Price (USD)')
    # axs[cnt].legend()
    axs[cnt].grid()

plt.subplots_adjust(hspace=0.25, wspace=0.15)
plt.tight_layout()
plt.show()







# ['Close', 'Dividends', 'High', 'Low', 'Open', 'T', 'Volume', '_AXIS_LEN', '_AXIS_ORDERS', '_AXIS_TO_AXIS_NUMBER', '_HANDLED_TYPES', '__abs__', '__add__', 
# '__and__', '__annotations__', '__array__', '__array_priority__', '__array_ufunc__', '__arrow_c_stream__', '__bool__', '__class__', '__contains__', '__copy__', 
# '__dataframe__', '__dataframe_consortium_standard__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__divmod__', '__doc__', '__eq__', 
# '__finalize__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
# '__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', '__init_subclass__', '__invert__', '__ior__', '__ipow__', '__isub__', '__iter__', '__itruediv__', 
# '__ixor__', '__le__', '__len__', '__lt__', '__matmul__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', 
# '__pandas_priority__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmatmul__', 
# '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', 
# '__str__', '__sub__', '__subclasshook__', '__truediv__', '__weakref__', '__xor__', '_accessors', '_accum_func', '_agg_examples_doc', '_agg_see_also_doc', 
# '_align_for_op', '_align_frame', '_align_series', '_append', '_arith_method', '_arith_method_with_reindex', '_as_manager', '_attrs', '_box_col_values', 
# '_can_fast_transpose', '_check_inplace_and_allows_duplicate_labels', '_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', 
# '_check_setitem_copy', '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', '_cmp_method', '_combine_frame', '_consolidate', '_consolidate_inplace', 
# '_construct_axes_dict', '_construct_result', '_constructor', '_constructor_from_mgr', '_constructor_sliced', '_constructor_sliced_from_mgr', 
# '_create_data_for_split_and_tight_to_dict', '_data', '_deprecate_downcast', '_dir_additions', '_dir_deletions', '_dispatch_frame_op', '_drop_axis', 
# '_drop_labels_or_levels', '_ensure_valid_index', '_find_valid_index', '_flags', '_flex_arith_method', '_flex_cmp_method', '_from_arrays', '_from_mgr', 
# '_get_agg_axis', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', 
# '_get_cleaned_column_resolvers', '_get_column_array', '_get_index_resolvers', '_get_item_cache', '_get_label_or_level_values', '_get_numeric_data', '_get_value', 
# '_get_values_for_csv', '_getitem_bool_array', '_getitem_multilevel', '_getitem_nocopy', '_getitem_slice', '_gotitem', '_hidden_attrs', '_indexed_same', 
# '_info_axis', '_info_axis_name', '_info_axis_number', '_info_repr', '_init_mgr', '_inplace_method', '_internal_names', '_internal_names_set', '_is_copy', 
# '_is_homogeneous_type', '_is_label_or_level_reference', '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_view', '_is_view_after_cow_rules', 
# '_iset_item', '_iset_item_mgr', '_iset_not_inplace', '_item_cache', '_iter_column_arrays', '_ixs', '_logical_func', '_logical_method', 
# '_maybe_align_series_as_frame', '_maybe_cache_changed', '_maybe_update_cacher', '_metadata', '_mgr', '_min_count_stat_function', '_needs_reindex_multi', 
# '_pad_or_backfill', '_protect_consolidate', '_reduce', '_reduce_axis1', '_reindex_axes', '_reindex_multi', '_reindex_with_indexers', '_rename', 
# '_replace_columnwise', '_repr_data_resource_', '_repr_fits_horizontal_', '_repr_fits_vertical_', '_repr_html_', '_repr_latex_', '_reset_cache', '_reset_cacher', 
# '_sanitize_column', '_series', '_set_axis', '_set_axis_name', '_set_axis_nocheck', '_set_is_copy', '_set_item', '_set_item_frame_value', '_set_item_mgr', 
# '_set_value', '_setitem_array', '_setitem_frame', '_setitem_slice', '_shift_with_freq', '_should_reindex_frame_op', '_slice', '_stat_function', 
# '_stat_function_ddof', '_take_with_is_copy', '_to_dict_of_blocks', '_to_latex_via_styler', '_typ', '_update_inplace', '_validate_dtype', '_values', '_where', 
# 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'apply', 'applymap', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 
# 'attrs', 'axes', 'backfill', 'between_time', 'bfill', 'bool', 'boxplot', 'clip', 'columns', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 
# 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 
# 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 
# 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 
# 'info', 'insert', 'interpolate', 'isetitem', 'isin', 'isna', 'isnull', 'items', 'iterrows', 'itertuples', 'join', 'keys', 'kurt', 'kurtosis', 'last', 
# 'last_valid_index', 'le', 'loc', 'lt', 'map', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 
# 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 
# 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 
# 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 
# 'set_index', 'shape', 'shift', 'size', 'skew', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 
# 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdown', 
# 'to_numpy', 'to_orc', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'to_xml', 'transform', 
# 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unstack', 'update', 'value_counts', 'values', 'var', 'where', 'xs']






# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', '__weakref__', '_analysis', '_data', '_download_options', '_earnings', '_earnings_dates', '_expirations', '_fast_info', 
# '_fetch_ticker_tz', '_financials', '_fundamentals', '_funds_data', '_get_ticker_tz', '_holders', '_isin', '_lazy_load_price_history', '_news', '_options2df', 
# '_price_history', '_quote', '_shares', '_tz', '_underlying', 'actions', 'analyst_price_targets', 'balance_sheet', 'balancesheet', 'calendar', 
# 'capital_gains', 'cash_flow', 'cashflow', 'dividends', 'earnings', 'earnings_dates', 'earnings_estimate', 'earnings_history', 'eps_revisions', 'eps_trend', 
# 'fast_info', 'financials', 'funds_data', 'get_actions', 'get_analyst_price_targets', 'get_balance_sheet', 'get_balancesheet', 'get_calendar', 'get_capital_gains', 
# 'get_cash_flow', 'get_cashflow', 'get_dividends', 'get_earnings', 'get_earnings_dates', 'get_earnings_estimate', 'get_earnings_history', 'get_eps_revisions', 
# 'get_eps_trend', 'get_fast_info', 'get_financials', 'get_funds_data', 'get_growth_estimates', 'get_history_metadata', 'get_income_stmt', 'get_incomestmt', 
# 'get_info', 'get_insider_purchases', 'get_insider_roster_holders', 'get_insider_transactions', 'get_institutional_holders', 'get_isin', 'get_major_holders', 
# 'get_mutualfund_holders', 'get_news', 'get_recommendations', 'get_recommendations_summary', 'get_revenue_estimate', 'get_sec_filings', 'get_shares', 
# 'get_shares_full', 'get_splits', 'get_sustainability', 'get_upgrades_downgrades', 'growth_estimates', 'history', 'history_metadata', 'income_stmt', 'incomestmt', 
# 'info', 'insider_purchases', 'insider_roster_holders', 'insider_transactions', 'institutional_holders', 'isin', 'major_holders', 'mutualfund_holders', 'news', 
# 'option_chain', 'options', 'proxy', 'quarterly_balance_sheet', 'quarterly_balancesheet', 'quarterly_cash_flow', 'quarterly_cashflow', 'quarterly_earnings', 
# 'quarterly_financials', 'quarterly_income_stmt', 'quarterly_incomestmt', 'recommendations', 'recommendations_summary', 'revenue_estimate', 'sec_filings', 
# 'session', 'shares', 'splits', 'sustainability', 'ticker', 'upgrades_downgrades']