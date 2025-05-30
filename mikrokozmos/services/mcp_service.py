import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, Optional

class MCPService:
    def __init__(self):
        self.base_url = "https://evds2.tcmb.gov.tr/service/evds"
        self.series = {
            "USD": "TP.DK.USD.A",
            "EUR": "TP.DK.EUR.A",
            "ALTIN": "TP.DK.ALTIN.A",
            "ENFLASYON": "TP.TG1.Y01",
            "FAIZ": "TP.TG2.Y01"
        }
    
    def get_economic_data(self) -> Dict[str, Optional[float]]:
        """Güncel ekonomik verileri çeker."""
        try:
            # Son 1 ayın verilerini al
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)
            
            data = {}
            for key, series in self.series.items():
                url = f"{self.base_url}/series={series}&startDate={start_date.strftime('%d-%m-%Y')}&endDate={end_date.strftime('%d-%m-%Y')}&type=json"
                response = requests.get(url)
                
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data and len(json_data) > 0:
                        # En son veriyi al
                        data[key] = float(json_data[-1]["value"])
                    else:
                        data[key] = None
                else:
                    data[key] = None
            
            return data
        except Exception as e:
            print(f"MCP veri çekme hatası: {str(e)}")
            return {key: None for key in self.series.keys()}
    
    def get_economic_context(self) -> str:
        """Ekonomik verileri karakterlerin anlayabileceği bir formatta döndürür."""
        data = self.get_economic_data()
        
        context = "Güncel Ekonomik Veriler:\n"
        if data["USD"]:
            context += f"Dolar: {data['USD']:.2f} TL\n"
        if data["EUR"]:
            context += f"Euro: {data['EUR']:.2f} TL\n"
        if data["ALTIN"]:
            context += f"Altın: {data['ALTIN']:.2f} TL\n"
        if data["ENFLASYON"]:
            context += f"Enflasyon: %{data['ENFLASYON']:.2f}\n"
        if data["FAIZ"]:
            context += f"Faiz: %{data['FAIZ']:.2f}\n"
        
        return context 