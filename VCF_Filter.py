import vcf

def fiterSNP(vcffile,SM, flagstatResult, readlength, Gsize, outputVcf):
    f = open(flagstatResult)
    mappedReads = f.readlines()[2].split()[0]
    TotalReadLength = int(mappedReads)*int(readlength)
    depth = TotalReadLength/float(Gsize)
    print 'Average Depth: %s'%depth

    vcffile = open(vcffile)
    myvcf = vcf.Reader(vcffile)

    outvcf = open(outputVcf, 'w')
    woutvcf = vcf.Writer(outvcf, myvcf)

    for i in myvcf:
        Genotype = i.genotype(SM)['GT']
        Type = i.INFO['TYPE'][0]
        if Genotype == '1/1' and Type == 'snp':
            Depth = i.genotype(SM)['DP']
            if 0.3*depth <=Depth<= 3*depth:
                woutvcf.write_record(i)
    vcffile.close()
    outvcf.close()
            
    

import sys
if len(sys.argv) ==7:
    fiterSNP(*sys.argv[1:])
else:
    print 'python FilterOneOneSNPsBasedOnDepth.py vcf sampleName flagstatResult readlength Genomesize output'
    
