# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from frappe import _


def get():
	return {
        _("Assets"): {
            "account_number": "1",
            "is_group": 1,
            "root_type": "Asset",
            _("Current Assets"): {
                "account_number": "10",
                "is_group": 1,
                _("Treasury"): {
                    "account_number": "100",
                    "is_group": 1,
                    _("Cash"): {
                        "account_number": "1000",
                        "account_type": "Cash"
                    },
                    _("Bank Balance"): {
                        "account_number": "1020",
                        "account_type": "Bank"
                    }
                },
                _("Short-Term Listed Securities"): {
                    "account_number": "106",
                    "is_group": 1,
                    _("Securities"): {
                        "account_number": "1060"
                    },
                    _("Value Adjustments on Securities"): {
                        "account_number": "1069"
                    }
                },
                _("Receivables from Sale of Goods and Services"): {
                    "account_number": "110",
                    "is_group": 1,
                    _("Receivables from Deliveries and Services (Debtors)"): {
                        "account_number": "1100"
                    },
                    _("Dél credere"): {
                        "account_number": "1109"
                    }
                },
                _("Other Short-Term Receivables"): {
                    "account_number": "114",
                    "is_group": 1,
                    _("Advances and Loans"): {
                        "account_number": "1140"
                    },
                    _("Value Adjustments on Advances and Loans"): {
                        "account_number": "1149"
                    },
                    _("VAT Tax Credit on Materials, Goods, Services, Energy"): {
                        "account_number": "1170"
                    },
                    _("VAT Tax Credit on Investments, Other Operating Expenses"): {
                        "account_number": "1171"
                    },
                    _("Withholding Tax"): {
                        "account_number": "1176"
                    },
                    _("Receivables from Social Security and Pension Institutions"): {
                        "account_number": "1180"
                    },
                    _("Withholding Tax at Source"): {
                        "account_number": "1189"
                    },
                    _("Other Short-Term Receivables"): {
                        "account_number": "1190"
                    },
                    _("Value Adjustments on Other Short-Term Receivables"): {
                        "account_number": "1199"
                    }
                },
                _("Inventories and Uninvoiced Services"): {
                    "account_number": "120",
                    "is_group": 1,
                    _("Commercial Goods"): {
                        "account_number": "1200"
                    },
                    _("Raw Materials"): {
                        "account_number": "1210"
                    },
                    _("Work Materials"): {
                        "account_number": "1220"
                    },
                    _("Auxiliary and Consumable Materials"): {
                        "account_number": "1230"
                    },
                    _("Consignment Commercial Goods"): {
                        "account_number": "1250"
                    },
                    _("Finished Goods"): {
                        "account_number": "1260"
                    },
                    _("Semi-Finished Goods"): {
                        "account_number": "1270"
                    },
                    _("Uninvoiced Services"): {
                        "account_number": "1280"
                    }
                },
                _("Prepaid Expenses"): {
                    "account_number": "130",
                    "is_group": 1,
                    _("Expenses Paid for the Following Period"): {
                        "account_number": "1300"
                    },
                    _("Income Not Yet Received"): {
                        "account_number": "1301"
                    }
                }
            },
            _("Fixed Assets"): {
                "account_number": "14",
                "is_group": 1,
                _("Financial Investments"): {
                    "account_number": "140",
                    "is_group": 1,
                    _("Securities"): {
                        "account_number": "1400"
                    },
                    _("Value Adjustments on Securities"): {
                        "account_number": "1409"
                    },
                    _("Loans"): {
                        "account_number": "1440"
                    },
                    _("Mortgages"): {
                        "account_number": "1441"
                    },
                    _("Value Adjustments on Long-Term Receivables"): {
                        "account_number": "1449"
                    }
                },
                _("Participations"): {
                    "account_number": "148",
                    "is_group": 1,
                    _("Participations"): {
                        "account_number": "1480"
                    },
                    _("Value Adjustments on Participations"): {
                        "account_number": "1489"
                    }
                },
                _("Tangible Movable Assets"): {
                    "account_number": "150",
                    "is_group": 1,
                    _("Machinery and Equipment"): {
                        "account_number": "1500"
                    },
                    _("Value Adjustments on Machinery and Equipment"): {
                        "account_number": "1509"
                    },
                    _("Furniture and Fixtures"): {
                        "account_number": "1510"
                    },
                    _("Value Adjustments on Furniture and Fixtures"): {
                        "account_number": "1519"
                    },
                    _("Office Machines, IT, Communication Technology"): {
                        "account_number": "1520"
                    },
                    _("Value Adjustments on Office Machines, IT, Communication Technology"): {
                        "account_number": "1529"
                    },
                    _("Vehicles"): {
                        "account_number": "1530"
                    },
                    _("Value Adjustments on Vehicles"): {
                        "account_number": "1539"
                    },
                    _("Tools and Instruments"): {
                        "account_number": "1540"
                    },
                    _("Value Adjustments on Tools and Instruments"): {
                        "account_number": "1549"
                    }
                },
                _("Tangible Immovable Assets"): {
                    "account_number": "160",
                    "is_group": 1,
                    _("Commercial Buildings"): {
                        "account_number": "1600"
                    },
                    _("Value Adjustments on Commercial Buildings"): {
                        "account_number": "1609"
                    }
                },
                _("Intangible Assets"): {
                    "account_number": "170",
                    "is_group": 1,
                    _("Patents, Know-how, Licenses, Rights, Developments"): {
                        "account_number": "1700"
                    },
                    _("Value Adjustments on Patents, Know-how, Licenses, Rights, Developments"): {
                        "account_number": "1709"
                    },
                    _("Goodwill"): {
                        "account_number": "1770"
                    },
                    _("Value Adjustments on Goodwill"): {
                        "account_number": "1779"
                    }
                },
                _("Unpaid Share Capital, Partnership Interests, or Foundation Interests"): {
                    "account_number": "180",
                    "is_group": 1,
                    _("Unpaid Share Capital, Partnership Interests, or Foundation Interests"): {
                        "account_number": "1850"
                    }
                }
            }
        },
        _("Liabilities"): {
        "account_number": "2",
        "is_group": 1,
        "root_type": "Liability",
            _("Short-Term Liabilities"): {
                "account_number": "20",
                "is_group": 1,
                _("Liabilities from Deliveries and Services"): {
                    "account_number": "200",
                    "is_group": 1,
                    _("Liabilities from Deliveries and Services (Creditors)"): {
                        "account_number": "2000"
                    },
                    _("Advances Received"): {
                        "account_number": "2030"
                    }
                },
                _("Short-Term Interest-Bearing Liabilities"): {
                    "account_number": "210",
                    "is_group": 1,
                    _("Bank Liabilities"): {
                        "account_number": "2100"
                    },
                    _("Financial Lease Liabilities"): {
                        "account_number": "2120"
                    },
                    _("Other Interest-Bearing Liabilities"): {
                        "account_number": "2140"
                    }
                },
                _("Other Short-Term Liabilities"): {
                    "account_number": "220",
                    "is_group": 1,
                    _("VAT Due (Turnover Tax)"): {
                        "account_number": "2200"
                    },
                    _("VAT Clearing Account"): {
                        "account_number": "2201"
                    },
                    _("Withholding Tax"): {
                        "account_number": "2206"
                    },
                    _("Direct Taxes"): {
                        "account_number": "2208"
                    },
                    _("Other Short-Term Liabilities"): {
                        "account_number": "2210"
                    },
                    _("Decided Distributions"): {
                        "account_number": "2261"
                    },
                    _("Social Security and Pension Institutions"): {
                        "account_number": "2270"
                    },
                    _("Wages Payable"): {
                        "account_number": "2271", "account_category": "Other Payables"
                    },
                    _("Withholding Tax at Source"): {
                        "account_number": "2279"
                    }
                },
                _("Accrued Expenses and Short-Term Provisions"): {
                    "account_number": "230",
                    "is_group": 1,
                    _("Expenses Not Yet Paid"): {
                        "account_number": "2300"
                    },
                    _("Income Received for the Following Period"): {
                        "account_number": "2301"
                    },
                    _("Short-Term Provisions"): {
                        "account_number": "2330"
                    }
                }
            },
            _("Long-Term Liabilities"): {
                "account_number": "24",
                "is_group": 1,
                _("Long-Term Interest-Bearing Liabilities"): {
                    "account_number": "240",
                    "is_group": 1,
                    _("Bank Liabilities"): {
                        "account_number": "2400"
                    },
                    _("Financial Lease Liabilities"): {
                        "account_number": "2420"
                    },
                    _("Bond Issues"): {
                        "account_number": "2430"
                    },
                    _("Loans"): {
                        "account_number": "2450"
                    },
                    _("Mortgages"): {
                        "account_number": "2451"
                    }
                },
                _("Other Long-Term Liabilities"): {
                    "account_number": "250",
                    "is_group": 1,
                    _("Other Long-Term Liabilities (Non-Interest Bearing)"): {
                        "account_number": "2500"
                    }
                },
                _("Provisions and Similar Statutory Items"): {
                    "account_number": "260",
                    "is_group": 1,
                    _("Provisions"): {
                        "account_number": "2600"
                    }
                }
            },
            _("Equity (Legal Entities)"): {
                "account_number": "28",
                "is_group": 1,
                _("Share Capital, Partnership Interests, or Foundation Interests"): {
                    "account_number": "280",
                    "is_group": 1,
                    _("Share Capital, Partnership Interests, or Foundation Interests"): {
                        "account_number": "2800"
                    }
                },
                _("Reserves and Net Income/Loss for the Period"): {
                    "account_number": "290",
                    "is_group": 1,
                    _("Legal Capital Reserve"): {
                        "account_number": "2900"
                    },
                    _("Reserve for Own Participations"): {
                        "account_number": "2930"
                    },
                    _("Revaluation Reserve"): {
                        "account_number": "2940"
                    },
                    _("Legal Profit Reserve"): {
                        "account_number": "2950"
                    },
                    _("Voluntary Profit Reserves"): {
                        "account_number": "2960"
                    },
                    _("Retained Earnings or Loss Carryforward"): {
                        "account_number": "2970"
                    },
                    _("Net Income or Loss for the Period"): {
                        "account_number": "2979"
                    },
                    _("Own Shares, Partnership Interests, or Foundation Interests (Negative Item)"): {
                        "account_number": "2980"
                    }
                }
            }
        },
        _("Operating Income from Deliveries and Services"): {
            "account_number": "3",
            "is_group": 1,
            "root_type": "Income",
            _("Manufacturing Income"): {
                "account_number": "3000"
            },
            _("Commercial Income"): {
                "account_number": "3200"
            },
            _("Service Income"): {
                "account_number": "3400"
            },
            _("Other Income from Deliveries and Services"): {
                "account_number": "3600"
            },
            _("Internal Services"): {
                "account_number": "3700"
            },
            _("Internal Consumption"): {
                "account_number": "3710"
            },
            _("Income Reductions"): {
                "account_number": "3800"
            },
            _("Losses on Receivables (Debtors), Change in Dél credere"): {
                "account_number": "3805"
            },
            _("Changes in Inventories of Semi-Finished Goods"): {
                "account_number": "3900"
            },
            _("Changes in Inventories of Finished Goods"): {
                "account_number": "3901"
            },
            _("Changes in Inventories of Uninvoiced Services"): {
                "account_number": "3940"
            }
        },
        _("Material, Goods, Services, and Energy Expenses"): {
            "account_number": "4",
            "is_group": 1,
            "root_type": "Expense",
            _("Production Material Expenses"): {
                "account_number": "4000"
            },
            _("Goods Expenses"): {
                "account_number": "4200"
            },
            _("Services Rendered Expenses"): {
                "account_number": "4400"
            },
            _("Production Energy Expenses"): {
                "account_number": "4500"
            },
            _("Expense Reductions"): {
                "account_number": "4900"
            }
        },
        _("Personnel Expenses"): {
            "account_number": "5",
            "is_group": 1,
            "root_type": "Expense",
            _("Salary Expenses"): {
                "account_number": "5200"
            },
            _("Social Security Expenses"): {
                "account_number": "5700"
            },
            _("Other Personnel Expenses"): {
                "account_number": "5800"
            },
            _("Third-Party Services"): {
                "account_number": "5900"
            }
        },
        _("Other Operating Expenses, Depreciation and Value Adjustments, and Financial Result"): {
            "account_number": "6",
            "is_group": 1,
            "root_type": "Expense",
            _("Real Estate Expenses"): {
                "account_number": "6000"
            },
            _("Maintenance, Repairs, Replacement of Tangible Movable Assets"): {
                "account_number": "6100"
            },
            _("Leasing Expenses for Tangible Movable Assets"): {
                "account_number": "6105"
            },
            _("Vehicle and Transport Expenses"): {
                "account_number": "6200"
            },
            _("Vehicle Leasing and Rental"): {
                "account_number": "6260"
            },
            _("Insurance, Taxes, Fees, Licenses"): {
                "account_number": "6300"
            },
            _("Energy and Disposal Expenses"): {
                "account_number": "6400"
            },
            _("Administrative Expenses"): {
                "account_number": "6500"
            },
            _("IT Expenses, Including Leasing"): {
                "account_number": "6570"
            },
            _("Advertising Expenses"): {
                "account_number": "6600"
            },
            _("Other Operating Expenses"): {
                "account_number": "6700"
            },
            _("Depreciation and Value Adjustments on Assets"): {
                "account_number": "6800"
            },
            _("Financial Expenses"): {
                "account_number": "6900"
            },
            _("Financial Income"): {
                "account_number": "6950"
            }
        },
        _("Ancillary Operating Result"): {
            "account_number": "7",
            "is_group": 1,
            "root_type": "Income",
            _("Income from Ancillary Activities"): {
                "account_number": "7000"
            },
            _("Expenses from Ancillary Activities"): {
                "account_number": "7010"
            },
            _("Operating Income from Real Estate"): {
                "account_number": "7500"
            },
            _("Operating Expenses from Real Estate"): {
                "account_number": "7510"
            }
        },
        _("Non-Operating, Exceptional, One-Time, or Prior Period Expenses and Income"): {
            "account_number": "8",
            "is_group": 1,
            "root_type": "Expense",
            _("Non-Operating Expenses"): {
                "account_number": "8000"
            },
            _("Non-Operating Income"): {
                "account_number": "8100"
            },
            _("Exceptional, One-Time, or Prior Period Expenses"): {
                "account_number": "8500"
            },
            _("Exceptional, One-Time, or Prior Period Income"): {
                "account_number": "8510"
            },
            _("Direct Taxes"): {
                "account_number": "8900"
            }
        },
        _("Closing"): {
            "account_number": "9",
            "is_group": 1,
            "root_type": "Equity",
            _("Net Income or Loss for the Period"): {
                "account_number": "9200"
            }
        }
    }
